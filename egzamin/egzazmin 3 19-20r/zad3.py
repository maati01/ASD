from zad3testy import runtests

#merguje po 2 linked listy
#O(nlogn)

class Node:
    def __init__( self, val ):
        self.next = None
        self.val = val

def merge(A,B):
    if A.val > B.val:
        start = B
        temp = B.next
        B.next = None
        B = temp
    else:
        start = A
        temp = A.next
        A.next = None
        A = temp

    head = start

    while A is not None and B is not None:
        if A.val > B.val:
            start.next = B
            temp = B.next
            B.next = None
            B = temp
        else:
            start.next = A
            temp = A.next
            A.next = None
            A = temp

        start = start.next

        if A is None:
            start.next = B
        if B is None:
            start.next = A

    return head



def tasks(T):
  n = len(T)
  length = n

  while length > 1:
    ind = 0

    for i in range(0,length - 1,2):
        T[ind] = merge(T[i], T[i+1])
        ind += 1

    length = ind

  if n % 2 != 0: #gdy jest nieparzysta liczb linked list merguje poza petla tą jedną dodatkową która została na koncu
      T[0] = merge(T[0],T[n-1])

  return T[0]

runtests( tasks )