import sys

from ioet_challenge.scheduler import ACME_Scheduler

if __name__ == '__main__':
    acme_scheduler = ACME_Scheduler()
    print(acme_scheduler.hello_world())
