class BSTNode:
    def __init__(self):
        self.G = None
        self.A = None
        self.T = None
        self.C = None
        self.end = False

#tworze BST ze wksaźnikami na G,A,T,C
#iteruje po stringu idac analogicznie po drzewie
#dostawiam węzły na kolejncyh literach jesli nie było takiego stringa
#zapisuje koniec
#jeśli jakiś string skończy sie w takim samym miejscu to znaczy że już wystąpił
#O(n*len_max_string)

def check_different_strings(T):
    n = len(T)

    tree = BSTNode()

    for i in range(n):
        root = tree
        k = len(T[i])
        for j in range(k):
            x = T[i][j]
            if T[i][j] == 'G' and root.G is not None:
                root = root.G
                continue
            elif T[i][j] == 'G' and root.G is None:
                root.G = BSTNode()
                root = root.G
                continue

            if T[i][j] == 'A' and root.A is not None:
                root = root.A
                continue
            elif T[i][j] == 'A' and root.A is None:
                root.A = BSTNode()
                root = root.A
                continue

            if T[i][j] == 'T' and root.T is not None:
                root = root.T
                continue
            elif T[i][j] == 'T' and root.T is None:
                root.T = BSTNode()
                root = root.T
                continue

            if T[i][j] == 'C' and root.C is not None:
                root = root.C
                continue
            elif T[i][j] == 'C' and root.C is None:
                root.C = BSTNode()
                root = root.C
                continue

        if root.end is True:
            return False
        else:
            root.end = True

    return True
test = ['GATC','GAT', 'GAC', 'GG']
print(check_different_strings(test))
test = ['GATC','GAT', 'GAC', 'GG', 'GATC']
print(check_different_strings(test))