from ioet_challenge.reader import Reader
from ioet_challenge.scheduler import ACME_Scheduler

if __name__ == '__main__':
    my_reader = Reader()
    my_reader.load_data()
    workers = my_reader.clean_data()
    for k in workers.keys():
        print(k)
        worker = workers[k]
        for d in worker.work.keys():
            print(d)
            print(worker.work[d])
    acme_scheduler = ACME_Scheduler(workers)
    acme_scheduler.calc_salaries()
    # print(acme_scheduler.hello_world())
