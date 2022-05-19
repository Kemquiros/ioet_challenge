weekdays = ["MO","TU","WE","TH","FR","SA","SU"]

class ACME_Scheduler:

    def __init__(self, workers):
        self.workers = workers
        self.pay_rate = {1: 25, 2: 15, 3: 20}

    def get_pay_rate(self,day,time_slot):
        result = self.pay_rate[time_slot]
        if day == "SA" or day == "SU":
            result += 5
        return result

    def calc_salary_same_slot(self, h_init, m_init, h_finish, m_finish):
        salary = h_finish - h_init
        if m_finish >= m_init:
            salary += (m_finish - m_init)/60
        else:
            salary -= 1
            salary += (60 - m_init + m_finish)/60
        return salary
    
    def select_slot(self, h_init, m_init):
        '''Select one slot according to the hour:minutes'''
        slot = None
        if (h_init == 0 and m_init >= 1) or (h_init > 0 and m_init >= 0 and h_init<=8 and m_init<=59) or (h_init == 9 and m_init == 0):
            slot = 1
        elif (h_init == 9 and m_init >= 1) or (h_init > 9 and m_init >= 0 and h_init<=17 and m_init<=59) or (h_init == 18 and m_init == 0):
            slot = 2
        elif (h_init == 18 and m_init >= 1) or (h_init > 18 and m_init >= 0 and h_init<=23 and m_init<=59) or (h_init == 0 and m_init == 0):
            slot = 3
        return slot

    def calc_salary_slot(self, d, h_init, m_init, h_finish, m_finish):
        '''Calculates the salary for each time slot'''
        salary = 0
        slot_init = self.select_slot(h_init, m_init)
        slot_finish = self.select_slot(h_finish, m_finish)

        if slot_init == 1:
            if slot_finish == 1:
                salary += self.calc_salary_same_slot(h_init, m_init, h_finish, m_finish)
                salary *= self.get_pay_rate(day=d,time_slot=slot_init)
            elif slot_finish == 2:
                salary = self.calc_salary_slot(d, h_init, m_init, 9, 0)
                salary += self.calc_salary_slot(d, 9, 1, h_finish, m_finish)
            elif slot_finish == 3:
                salary = self.calc_salary_slot(d, h_init, m_init, 9, 0) 
                salary += self.calc_salary_slot(d, 9, 1, 18, 0)
                salary += self.calc_salary_slot(d, 18, 1, h_finish, m_finish)
        elif slot_init == 2:
            if slot_finish == 2:
                salary += self.calc_salary_same_slot(h_init, m_init, h_finish, m_finish)
                salary *= self.get_pay_rate(day=d,time_slot=slot_init)
            elif slot_finish == 3:
                salary = self.calc_salary_slot(d, h_init, m_init, 18, 0)
                salary += self.calc_salary_slot(d, 18, 1, h_finish, m_finish)
        elif slot_init == 3 and slot_finish == 3:
                salary += self.calc_salary_same_slot(h_init, m_init, h_finish, m_finish)
                salary *= self.get_pay_rate(day=d,time_slot=slot_init)

        return salary


    def calc_salary(self, worker):
        '''For each worker calculates the salary'''
        salary = 0
        for day in weekdays:
            for slot in worker.work[day]:
                slot_init, slot_finish = slot.split("-")
                hour_init, minutes_init = slot_init.split(":")
                hour_finish, minutes_finish = slot_finish.split(":")
                salary_slot = self.calc_salary_slot(day, int(hour_init), int(minutes_init), int(hour_finish), int(minutes_finish))
                salary += salary_slot
        return salary

    def calc_salaries(self):
        '''For every worker calculates the salary'''
        for worker_name in self.workers.keys():
            worker = self.workers[worker_name]
            worker.salary = self.calc_salary(worker)