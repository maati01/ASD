from displayBST import display

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.cnt = 1 #liczba węzłów w danym poddrzewie

def find(root, key):
    while root != None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right

    return None

def add(root, key): #dodawanie rekurencyjne, wuzględniająć liczbę węzłów
    if find(root,key) is not None:
        return root

    if root is None:
        root = BSTNode(key)
    elif key < root.key:
        root.cnt += 1
        root.left = add(root.left, key)
    elif key > root.key:
        root.cnt += 1
        root.right = add(root.right, key)


    return root

def find_i_value(root,i):
    ind = 1
    if root.left is not None:
        ind = root.left.cnt + 1


    while ind != i :
        if ind > i: #ide w lewo
            root = root.left
            if root.right is not None:
                ind = ind - root.right.cnt - 1 #obecny indeks, indeks parenta - ilosc prawego poddrzewa - 1
            else:
                ind -= 1
        else: #ide w prawo
            root = root.right
            if root.left is not None:
                ind = ind + root.left.cnt + 1 #obecny indeks, indeks parenta + ilosc lewego poddrzewa + 1
            else:
                ind += 1

    return root.key



tree = BSTNode(10)
tree = add(tree,7)
tree = add(tree,12)
tree = add(tree,5)
tree = add(tree,9)
tree = add(tree,2)
tree = add(tree,6)
tree = add(tree,12)
tree = add(tree,30)
tree = add(tree,20)
tree = add(tree,35)
tree = add(tree,18)
tree = add(tree,19)
display(tree)
print(find_i_value(tree,10))
print(find_i_value(tree,5))
print(find_i_value(tree,4))
print(find_i_value(tree,11))
print(find_i_value(tree,12))
print(find_i_value(tree,6))