from ioet_challenge.printer import print_results
from ioet_challenge.reader import Reader
from ioet_challenge.scheduler import AcmeScheduler

if __name__ == '__main__':
    my_reader = Reader()
    my_reader.load_data()
    workers = my_reader.clean_data()

    acme_scheduler = AcmeScheduler(workers)
    acme_scheduler.calc_salaries()

    print_results(workers)
