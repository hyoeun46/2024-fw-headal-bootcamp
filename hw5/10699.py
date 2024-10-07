from datetime import datetime

class date:
    def __init__(self):
        self.date = datetime.now()

    def input_date(self):
        return self.date.strftime("%Y-%m-%d")
    
    def print_date(self):
        print(self.input_date())

date = date()
date.print_date()