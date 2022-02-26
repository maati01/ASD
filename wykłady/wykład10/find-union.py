#implementacja find union z wykładu na lasach zbiorów rozłącznych
#dla m operacji, z czego n to make set to zlożoność O(mlogn) (zakładając łączenie wg rangi bez kompresji ścieżki)

class Node:
    def __init__(self,val):
        self.val = val
        self.rank = 0 #oszacowanie wysokości drzewa, nie bedzie dokladne
        self.parent = self

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)

    return x.parent

def union(x,y):
    x = find(x) #szukam reprezentanta zbioru
    y = find(y)

    if x == y: return #sytacja gdy sa w tym samym zbiorze

    if x.rank > y.rank: #"przyklejam" y do x, wysokość drzewa nie wzrosłą
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank: #potencjalnie drzewo mogło urosnąć
            y.rank += 1

A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
union(A,B)
union(C,D)
union(B,C)
find(D)