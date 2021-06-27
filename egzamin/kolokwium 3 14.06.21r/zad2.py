from zad2testy import runtests
from math import inf

class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

def find_min_sum(T):
    if T is None:
        return 0

    if T.right is None and T.left is None: #liść
        return inf

    res = T.value

    return min(res,find_min_sum(T.left) + find_min_sum(T.right))


def cutthetree(T):
    return find_min_sum(T.left) + find_min_sum(T.right) #zakładamy że nie ma połączenia root -> liść

runtests(cutthetree)