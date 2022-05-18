import sys

from ioet_challenge.worker import Worker

class Reader:

    def __init__(self, path="./data/data1.txt"):
        self.path = path
        self.data = []

    def load_data(self):
        file_handler = None
        try:
            file_handler = open(self.path)
        except FileNotFoundError:
            print("File " + self.path + " can't be opened",file=sys.stderr)
            exit(0)
        if file_handler:
            for line in file_handler:
                line = line.strip().strip("\n")
                self.data.append(line)
            file_handler.close()

    def clean_data(self):
        workers = {}
        for line in self.data:
            worker_name, worker_hours = line.split("=")
            if worker_name not in workers.keys():
                new_worker = Worker(worker_name)
                workers[worker_name] = new_worker
            worker = workers[worker_name]
            worker_slots = worker_hours.split(",")
            for slot in worker_slots:
                day = slot[0:2]
                hours = slot[2:]
                worker.add_work_slot(day,hours)
        return workers