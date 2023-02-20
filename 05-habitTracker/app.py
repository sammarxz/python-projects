import datetime

from habit import Habit

class HabitTracker:
    DATE_FORMAT = "%d/%m/%Y"

    def __init__(self):
        self.habits = {}
        self.today = datetime.date.today()

    def add_habit(self, name):
        self.habits[name] = Habit(name)

    def remove_habit(self, name):
        del self.habits[name]

    def mark_habit_done(self, name, date = None):
        date = self.today if not date else datetime.datetime.strptime(date, self.DATE_FORMAT).date()
        habit = self.habits[name]
        habit.add_completed_date(date)

    def mark_habit_undone(self, name, date = None):
        date = self.today if not date else datetime.datetime.strptime(date, self.DATE_FORMAT).date()
        habit = self.habits[name]
        habit.remove_completed_date(date)
    
    def print_habits(self):
        for name, habit in self.habits.items():
            completed_dates = habit.get_completed_dates()
            dates = [habit.strftime(self.DATE_FORMAT) for habit in completed_dates]
            print("{} | {}".format(name, (', ').join(dates) if completed_dates else '-' ))


tracker = HabitTracker()

tracker.add_habit("Fazer exercícios")
tracker.add_habit("Leitura")
tracker.add_habit("Sair com o cachorro")

tracker.mark_habit_done("Leitura", "19/02/2023")
tracker.mark_habit_done("Fazer exercícios")

tracker.mark_habit_done("Sair com o cachorro", "19/02/2023")

tracker.print_habits()