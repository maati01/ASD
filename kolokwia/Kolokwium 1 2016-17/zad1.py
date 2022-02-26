class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def insert(head, val):
    curr = head
    if curr.next == None:
        curr.next = Node(val)
    else:
        temp = curr.next
        curr.next = Node(val)
        curr.next.next = temp

def find_bucket(val, n, minimum, maximum): #funkcja przydziela bucketa uwzględniająć liczby ujemne
    _i = int((val - minimum) / (maximum - minimum) * n)
    if _i == n: _i -= 1

    return _i


def display(head):
    curr = head
    while curr is not None:
        print(curr.val, end=' ')
        curr = curr.next
    print()

def get_min(curr):
  curr_min = curr

  while curr is not None:
    if curr.val < curr_min.val:
      curr_min = curr
    curr = curr.next

  return curr_min


def selection_sort(head):
  curr = head.next
  while curr is not None:
    min_node = get_min(curr)
    curr.val, min_node.val = min_node.val, curr.val
    curr = curr.next

  return head

def sort(L):
    head = L #jeden wskaźnik potrdzeny do znalezienia dlugosci
    curr = L.next #drugi wskaźnik potrzebny wstawienia wartosci w odpowiednie bukcety
    head1 = L #ostatni wskaźnik potrzebny do przepinania juz posortowanych bucketów
    length = 0
    minimum = L.next.val
    maksimum = L.next.val

    while head.next != None: #sprawdzam maks,min i len O(n)
        length += 1
        head = head.next
        if head.val > maksimum:
            maksimum = head.val
        if head.val < minimum:
            minimum = head.val

    buckets = []
    for i in range(length): #tworze buckety
        buckets.append(Node("*", None))


    while curr != None: #wstawiam wartosci do odpowiednich bucketów
        insert(buckets[find_bucket(curr.val,length,minimum,maksimum)],curr.val)
        curr = curr.next

    for i in range(length): #sortuje buckety
        buckets[i] = selection_sort(buckets[i])

    for i in range(length): #przepinam wskazniki miedzy bucketami
        if buckets[i].next == None:
            continue
        buckets[i] = buckets[i].next
        head1.next = buckets[i]
        while buckets[i].next != None:
            buckets[i] = buckets[i].next
        head1 = buckets[i]

    return L.next

'''p = Node("*", None)
insert(p, 4)
insert(p, 2)
insert(p, 1)
insert(p, 5)
insert(p, 6)
insert(p, 7)
insert(p, 3)
insert(p, 9)
insert(p, 8)
insert(p, 10)
insert(p, -1)
insert(p, 0)
insert(p, 0)
insert(p, 13)
insert(p, -3)
insert(p, -3)
insert(p, -3)
insert(p, -3)
insert(p, 5)
p = sort(p)
display(p)'''


### test
def list2tab(A):
  if A is None:
    return []

  res = []
  while A is not None:
    res.append(A.val)
    A = A.next

  return res

def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.val = A[i]
    C.next = X
    C = X
  return H

def array_to_list(A):
  head = Node()
  curr = head
  for e in A:
    curr.next = Node(e)
    curr = curr.next

  return head

def display1(head):
  if head is None:
    print('Empty')
    return

  curr = head
  while curr is not None:
    print(curr.val, end=' ')
    curr = curr.next
  print()

##########################################################################
# random test sort
from testy import  test_linked_lists
from random import randint, seed
from time import time
def test_sort():
  rr = (-10**6, 10**6)
  n = 10**6
  m = 10
  sort_func = sort
  print_res = False

  for i in range(m):
    t = [randint(rr[0], rr[1]) for _ in range(n)]
    expected_res = sorted(t)

    if print_res: print('input:   ', t)
    start = time()
    t = list2tab(sort_func(array_to_list(t)))
    stop = time()
    if print_res: print('output:  ', t)

    res = 'INCORRECT'
    if t == expected_res:
      res = 'CORRECT'

    print('result:  ', res)
    print('time:    ', stop-start, '\n')

    if res == 'INCORRECT':
      break

test_sort()

#test_linked_lists.test_sort(sort,  10**6, 10, (- 10**7, 10 ** 7), False)
