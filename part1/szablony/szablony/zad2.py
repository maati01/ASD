from zad2testy import runtests
#Mateusz Powęska
#sortuje mniejsze linked listy które mają zakres co k
#nastepnie merguje pod listy które posortowałem, przejscie liniowe jest mniejsze od nlogn
#dla k = O(1)  czas nlogn
#dla k = O(logn)  czas(logn)(n)log(n)
#dla k = O(n)  czas n^2logn
#dodatkowa pamiec to k, tyle utworze nowych list

class Node:
    def __init__(self, val=None, next=None):
        self.val = None
        self.next = None


def get_min(curr):
    curr_min = curr

    while curr is not None:
        if curr.val < curr_min.val:
            curr_min = curr
        curr = curr.next

    return curr_min


def selection_sort(head):
    x = 0
    curr = head.next
    while curr is not None:
        x += 1
        min_node = get_min(curr)
        curr.val, min_node.val = min_node.val, curr.val
        curr = curr.next

    return head


def merge(p1, p2):
    head = p1
    prev1 = p1
    p1 = p1.next
    p2 = p2.next
    # Wstawiamy z p2 do p1
    while p2 is not None:
        while p1 is not None and p1.val < p2.val:
            prev1 = p1
            p1 = p1.next

        prev1.next = p2
        temp = p2.next
        p2.next = p1
        p2 = temp
        prev1 = prev1.next

    return head


def find(head):
    prev = head
    curr = head.next

    while curr is not None and prev.val < curr.val:
        prev = curr
        curr = curr.next

    return prev


def mergesort(l):
    curr = l

    while True:
        ser1 = find(curr)
        if ser1.next is None:
            if curr is l:
                return l
            else:
                curr = l
                continue

        ser2 = find(ser1.next)

        merged = merge(curr, ser1)

        if ser2.next is None:
            if curr is l:
                return merged
            else:
                curr = ser2.next


def SortH(p, k):
    lists = [Node]
    curr = p
    head = p
    head1 = p
    head2 = None

    length = 0
    while head.next != None: #sprawdzam maks,min i len O(n)
        length += 1
        head = head.next

    lists = []
    for i in range(length): #tworze buckety
        lists.append(Node("*", None))

    while curr.next != None:
        head1 = selection_sort(curr)

    return p


runtests(SortH)
