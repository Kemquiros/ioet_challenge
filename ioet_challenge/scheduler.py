weekdays = ["MO","TU","WE","TH","FR","SA","SU"]
class ACME_Scheduler:

    def __init__(self, workers):
        self.workers = workers
    
    def calc_salary_slot(self, d, h_init, m_init, h_finish, m_finish):
        salary = 0
        if d == "SA" or d == "SU":
            pass
        elif d == "MO" or d == "TU" or d == "WE" or d == "TH" or d == "FR":
            pass
        else:
            pass
        return salary


    def calc_salary(self, worker):
        salary = 0
        for day in weekdays:
            for slot in worker.work[day]:
                slot_init, slot_finish = slot.split("-")
                hour_init, minutes_init = slot_init.split(":")
                hour_finish, minutes_finish = slot_finish.split(":")
                salary += self.calc_salary_slot(day, int(hour_init), int(minutes_init), int(hour_finish), int(minutes_finish))


    def calc_salaries(self):
        for worker_name in self.workers.keys():
            worker = self.workers[worker_name]
            self.calc_salary(worker)

    def hello_world(self) -> str:
        return "Hello World!"