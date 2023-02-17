import json

def show_menu():
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Excluir tarefa")
    print("5. Sair")

def add_task():
    task = input("Digite a tarefa a ser adicionada: ")
    with open("todo.json", "r") as todo_file:
        tasks = json.load(todo_file)
    with open("todo.json", "w") as todo_file:
        tasks.append({"description": task, "done": False})
        json.dump(tasks, todo_file)
    print("Tarefa adicionada com sucesso.")

def view_tasks():
    with open("todo.json", "r") as todo_file:
        tasks = json.load(todo_file)
        if len(tasks) == 0:
            print("Não há tarefas a fazer.")
        else:
            for index, task in enumerate(tasks):
                status = "concluída" if task["done"] else "a fazer"
                print(f"{index+1}. {task['description']} ({status})")

def complete_task():
    view_tasks()
    task_index = int(input("Digite o número da tarefa concluída: "))
    with open("todo.json", "r") as todo_file:
        tasks = json.load(todo_file)
    with open("todo.json", "w") as todo_file:
        for index, task in enumerate(tasks):
            if index == task_index-1:
                task["done"] = True
        json.dump(tasks, todo_file)
    print("Tarefa concluída com sucesso.")

def delete_task():
    view_tasks()
    task_index = int(input("Digite o número da tarefa a ser excluída: "))
    with open("todo.json", "r") as todo_file:
        tasks = json.load(todo_file)
    with open("todo.json", "w") as todo_file:
        for index, task in enumerate(tasks):
            if index == task_index-1:
                del tasks[index]
                break
        json.dump(tasks, todo_file)
    print("Tarefa excluída com sucesso.")

while True:
    show_menu()
    choice = int(input("Digite a opção desejada: "))
    if choice == 1:
        add_task()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        complete_task()
    elif choice == 4:
        delete_task()
    elif choice == 5:
        break
    else:
        print("Opção inválida. Tente novamente.")