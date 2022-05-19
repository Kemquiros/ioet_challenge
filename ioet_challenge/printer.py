def print_results(workers):
    '''Show the worker\'s payment in the screen'''
    for key in list(workers.keys()):
        worker = workers[key]
        print(f"The amount to pay {worker.name} is: {worker.salary} USD")
