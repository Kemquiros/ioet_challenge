class Printer:
    def print_results(self, workers):
        for key in list(workers.keys()):
            worker = workers[key]
            print("The amount to pay %s is: %d USD" % ( worker.name, worker.salary))