class Habit:
    def __init__(self, name):
        self.name = name
        self.completed_dates = set()

    def add_completed_date(self, date):
        self.completed_dates.add(date)

    def remove_completed_date(self, date):
        self.completed_dates.remove(date)
    
    def get_completed_dates(self):
        return self.completed_dates
