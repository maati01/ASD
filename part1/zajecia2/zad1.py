class Node:
    def __init__(self):
        self.next = None
        self.value = None


def tab_to_list(A):  # funkcja Falisza
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X

    return H.next


def print_list(L):  # funkcja Falisza
    while L != None:
        print(L.value, "->", end=' ')
        L = L.next
    print("|")


def cut_list(a):
    curr = a

    if a is None:
        return None, None

    while a.next is not None and a.value <= a.next.value:
        a = a.next

    new_head = a.next
    a.next = None

    return curr, new_head


def merge(a, b):  # scalanie dwóch posortowanych list
    head = Node()
    curr = head

    while a is not None and b is not None:
        if b.value >= a.value:
            curr.next = a
            a = a.next
        else:
            curr.next = b
            b = b.next

        curr = curr.next

    if a is None and b is not None:
        curr.next = b
    elif b is None and a is not None:
        curr.next = a

    while curr.next is not None:
        curr = curr.next

    return head.next, curr


def merge_natural_series_list(head):
    while True:
        new_head = None
        temp_tail = None
        while True:
            first_head, second_head = cut_list(head)

            if second_head is None and new_head is None:
                return first_head

            if second_head is None:
                break

            second_head, third_head = cut_list(second_head)

            last_tail = temp_tail
            temp_head, temp_tail = merge(first_head, second_head)

            if new_head is None:
                new_head = temp_head

            if third_head is None:
                break

            else:
                if last_tail is not None:
                    last_tail.next = temp_head
                temp_tail.next = third_head
                head = third_head

        head = new_head


A = [1, 3, 10]
B = [1, 1, 2, 3, 4, 11]
A = tab_to_list(A)
B = tab_to_list(B)
A = merge(A, B)
# print_list(A[0])
C = tab_to_list([1, 2, 5, 6, 2, 4, 10, 99, 1, 100, 101])
C = merge_natural_series_list(C)
print_list(C)
res_C = tab_to_list(sorted([1, 2, 5, 6, 2, 4, 10, 99, 1, 100, 101]))
print_list(res_C)
D = tab_to_list([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
D = merge_natural_series_list(D)
print_list(D)
res_D = tab_to_list(sorted([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]))
print_list(res_D)
E = tab_to_list([3, 2, 1])
E = merge_natural_series_list(E)
print_list(E)
F = tab_to_list([3, 2, 1, 0, 1, 2, 3, 4, 3, 2, -1, -2, -3])
res_F = tab_to_list(sorted([3, 2, 1, 0, 1, 2, 3, 4, 3, 2, -1, -2, -3]))
F = merge_natural_series_list(F)
print_list(res_F)
print_list(F)
