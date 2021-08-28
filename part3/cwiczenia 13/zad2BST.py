# ide max do lewego liscia
# przetwarzam go
# wracam
# jesli wracam z lewej strony ide raz w prawo i ppotem max w lewo
# gdy wrócę z prawej strony lub z lewej to wierzchołek jest przetworzony
# powtarzam
# O(n)

from displayBST import display

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

def find(root, key):
    while root != None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right

    return None

def add(root, key, prev=None):  # dodawanie rekurencyjne, wuzględniająć liczbę węzłów
    if find(root, key) is not None:
        return root

    if root is None:
        if prev is None:
            root = BSTNode(key)
        else:
            root = BSTNode(key)
            root.parent = prev
    elif key < root.key:
        root.left = add(root.left, key, root)
    elif key > root.key:
        root.right = add(root.right, key, root)

    return root

def values_sum(tree):
    tree_sum = 0
    left = False  # do sprawdzania czy którą krawędzią wracałęm
    right = False

    if tree.left is not None:
        root = tree.left
    else:
        root = tree.right

    prev = root

    while True:

        if root.parent is None and right:
            return tree_sum + root.key

        while root.left is not None and not left: #ide max w lewo
            prev = root
            root = root.left


        if root.left is None and root.right is None: #dodaje liść
            tree_sum += root.key

        if root.right is not None and not right: #moge isc w prawo jeden krok
            prev = root
            root = root.right
            left = False
            continue

        if right or left: #gdy wracam z lewej lub prawej strony i nie jestem w lisciu
            tree_sum += root.key

        if prev == root and right: #wracam do góry po drzewie
            prev = prev.parent

        if prev.key > root.key: #sprawdzam czy wróciłem z lewej
            left = True
            right = False
            root = prev
            prev = prev.parent
        elif prev.key < root.key: #sprawdzam czy wróciłem z prawej
            right = True
            left = True
            root = prev
            prev = prev.parent


tree = BSTNode(10)
tree = add(tree, 7)
tree = add(tree, 12)
tree = add(tree, 5)
tree = add(tree, 9)
tree = add(tree, 2)
tree = add(tree, 6)
tree = add(tree, 12)
tree = add(tree, 30)
tree = add(tree, 20)
tree = add(tree, 35)
tree = add(tree, 18)
tree = add(tree, 19)
display(tree)
print(values_sum(tree))
print()
tree1 = BSTNode(10)
tree1 = add(tree1,20)
tree1 = add(tree1,30)
display(tree1)
print(values_sum(tree1))
print()
tree2 = BSTNode(1)
tree2 = add(tree2,5)
tree2 = add(tree2,3)
tree2 = add(tree2,4)
tree2 = add(tree2,2)
display(tree2)
print(values_sum(tree2))