# random test sort
from random import randint
from time import time


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def test_sort(sort_func, arr_size, tests, rr, print_res):
    counter = 0
    for i in range(tests):
        tab = [randint(rr[0], rr[1]) for _ in range(arr_size)]
        if i == tests - 1:
            tab = []
        expected_res = sorted(tab)

        if print_res: print('input:   ', tab)
        start = time()
        tab = sort_func(tab)
        stop = time()
        if print_res: print('output:  ', tab)

        res = f"{bcolors.FAIL}INCORRECT{bcolors.ENDC}"
        if tab == expected_res:
            res = f"{bcolors.OKGREEN}CORRECT{bcolors.ENDC}"
            counter += 1

        print('result:  ', res)
        print('time:    ', stop - start, '\n')

        # if res == f"{bcolors.WARNING}INCORRECT{bcolors.ENDC}":
        #     break

    final = f'{bcolors.WARNING}{counter}/{tests}{bcolors.ENDC}'
    if counter == tests:
        final = f'{bcolors.OKGREEN}{counter}/{tests}{bcolors.ENDC}'

    print(f'final result:   {final} tests passed')
