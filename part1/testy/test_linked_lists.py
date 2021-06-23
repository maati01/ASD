from random import randint, seed
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


class Node:
    def __init__(self):
        self.next = None
        self.val = None


def list2tab(A):
    if A is None:
        return []

    res = []
    while A is not None:
        res.append(A.val)
        A = A.next

    return res


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.val = A[i]
        C.next = X
        C = X
    return H.next


def test_sort(sort_func, arr_size=100, tests=100, rr=(0, 10), print_res=True):
    counter = 0
    all_counter = 0
    seed(420)
    for i in range(tests):
        t = [randint(rr[0], rr[1]) for _ in range(arr_size)]
        expected_res = sorted(t)

        if print_res: print('input:   ', t)
        start = time()
        t = list2tab(sort_func(tab2list(t)))
        stop = time()
        if print_res: print('output:  ', t)

        res = f"{bcolors.FAIL}INCORRECT{bcolors.ENDC}"
        if t == expected_res:
            res = f"{bcolors.OKGREEN}CORRECT{bcolors.ENDC}"
            counter += 1
        all_counter += 1

        print(f'test number #{all_counter}/{tests}')
        print('result:  ', res)
        print('time:    ', stop - start, '\n')


    # if res == 'INCORRECT':
    #     break

    final = f'{bcolors.WARNING}'
    if counter == tests:
        final = f'{bcolors.OKGREEN}'

    print(f'final result:   {final}{counter}/{tests}{bcolors.ENDC} tests passed')