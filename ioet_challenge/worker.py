weekdays = ["MO","TU","WE","TH","FR","SA","SU"]

class Worker:
    '''Class to cover the worker abstraction'''
    def __init__(self, name:str):
        self.name = name
        self.work = {}
        self.salary = None
        self.init_weekdays()

    def init_weekdays(self) -> None:
        '''Initialize empty arrays for each day'''
        for day in weekdays:
            self.work[day] = []

    def add_work_slot(self, day: str, hours: str) -> bool:
        '''Add worked slot in the worker\'s record'''
        if day in weekdays:
            self.work[day].append(hours)
            return True
        return False