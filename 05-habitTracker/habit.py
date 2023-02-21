from datetime import datetime

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
    
    def get_habit(self, date_format):
        str_dates = [date.strftime(date_format) for date in self.completed_dates]
        str_dates.sort(key=lambda date: datetime.strptime(date, date_format))
        return {
            "habit": self.name,
            "completed_days": len(self.completed_dates),
            "completed_dates": ", ".join(str_dates),
        }
