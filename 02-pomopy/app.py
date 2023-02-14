import time

from messages import title, welcome_input
from config import TIMER, MAX_SESSIONS
from clear import clear
from notification import show_notification


def show_session(count):
    TIMER = [
        {
            "title": "Focus Time!",
            "time": 2
        },
        {
            "title": "Take a Break!",
            "time": 2
        },
        {
            "title": "Rest Time!",
            "time": 2
        },
    ]
    actual_session = TIMER[-1] if count == MAX_SESSIONS else TIMER[count % 2]
    actual_session_title = actual_session["title"]

    print(actual_session_title, end="\n")
    show_notification(actual_session_title)

    while actual_session["time"]:
        session_minutes, session_seconds = divmod(actual_session["time"], 60)
        print("{:02d}:{:02d}".format(session_minutes, session_seconds), end="\r")
        time.sleep(1)
        actual_session["time"]-= 1

def start():
    count = 0
    task_title = input("Give your section a name: ")

    while count <= MAX_SESSIONS:
        clear()
        print(task_title)
        print("-----------------------")
        show_session(count)
        count+= 1

if __name__ == "__main__":
    while True:
        clear()
        print(title)
        answer = input(welcome_input)
        
        if str.lower(answer) == "q":
            break
        else:
            start()

    print("Pomodoro Finished!")