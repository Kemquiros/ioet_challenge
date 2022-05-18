weekdays = ["MO","TU","WE","TH","FR","SA","SU"]
class Worker:
    def __init__(self, name:str):
        self.name = name
        self.work = {}
        self.salary = None
        self.init_weekdays()
    
    def init_weekdays(self):
        for day in weekdays:
            self.work[day] = []

    def add_work_slot(self, day: str, hours: str) -> bool:
        if day in weekdays:
            self.work[day].append(hours)
            return True
        return False