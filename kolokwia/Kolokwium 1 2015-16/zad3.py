class Node():
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next


def to_list(p):
    arr = []
    while p is not None:
        arr.append(p.val)
        p = p.next
    print(arr)


def insert(l, node):
    curr = l
    if curr.val >= node.val:
        node.next = curr
        return node

    prev = curr
    curr = curr.next
    while curr is not None and curr.val < node.val:
        prev = curr
        curr = curr.next
    prev.next = node
    node.next = curr

    return l


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.val = A[i]
        C.next = X
        C = X
    return H.next


def fixs_sorted_list(L):
    if L.next == None:
        return L

    curr = L.next
    prev = L
    upcoming = L.next.next

    if upcoming == None: #przypadek dla dwóch elementów
        if prev.val <= curr.val:
            return L
        else:
            curr.next = prev
            prev.next = None
            return curr

    if prev.val > curr.val and prev.val > upcoming.val: #przypadek gdy zly element jest na pierwszym miejscu
        prev.next = None
        return insert(curr,prev)

    while upcoming != None and prev.val <= curr.val <= upcoming.val:
        prev = curr
        curr = upcoming
        upcoming = upcoming.next

    if upcoming == None and curr.val < prev.val: #gdy zły element jest ostatni
        prev.next = None
        return insert(L, curr)

    elif upcoming == None and prev.val <= curr.val: #gdy wszysktko jest ok
        return L

    else: #gdy element jest "gdzies w srodku"
        if upcoming.val < curr.val: #gdy zły jest na nastepnej pozycji wzgledem curra
            curr.next = upcoming.next
            return insert(L,upcoming)

        else:
            prev.next = upcoming
            return insert(L, curr)

    return L


#tab = [50,100,200,49]
#tab = [50,55,100,56]
#tab = [101,1,2]
#tab = [1,2,3]
tab = [2,1]
tab = tab2list(tab)
tab = fixs_sorted_list(tab)
to_list(tab)
