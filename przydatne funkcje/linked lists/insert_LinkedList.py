class Node():
    def __init__(self, val, next):
        self.val = val
        self.next = next


def to_list(p):
    arr = []
    while p is not None:
        arr.append(p.val)
        p = p.next
    print(arr)


def insert(l, val):
    p = l
    if p.next is None:
        p.next = Node(val, None)
        return p

    prev = p
    p = p.next
    while p is not None and p.val < val:
        prev = p
        p = p.next
    q = Node(val, prev.next)
    prev.next = q
    return l


p = Node("*", None)
p = insert(p, 4)
p = insert(p, 2)
p = insert(p, 3)
p = insert(p, 6)
to_list(p)
