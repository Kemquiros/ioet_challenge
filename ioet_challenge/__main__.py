from ioet_challenge.printer import Printer
from ioet_challenge.reader import Reader
from ioet_challenge.scheduler import ACME_Scheduler

if __name__ == '__main__':
    my_reader = Reader()
    my_reader.load_data()
    workers = my_reader.clean_data()

    acme_scheduler = ACME_Scheduler(workers)
    acme_scheduler.calc_salaries()

    my_printer = Printer()
    my_printer.print_results(workers)
