class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

def find(root,key):
    while root != None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right

    return False

def find_next(root, key):
    root = find(root, key)
    if root is None:
        return None
    elif root.right is None:  # sytacja gdy nie moge isc w prawo
        if root.parent is None:  # sytacja gdy mamy samego roota
            return root
        else:
            while root.key > root.parent.key:  # ide w góre, aż przejde po wiekszym kluczu
                root = root.parent
                if root.parent is None:  # sytacja gdy nie ma nastepnika
                    return None
            return root.parent.key

    root = root.right

    while root.left != None:  # sytacja gdy moge isc raz w prawo i ciagle w lewo
        root = root.left

    return root.key


def insert(root, key):
    curr = root
    prev = None
    left = False
    if curr is None:
        root = BSTNode(key)
        return root

    while curr is not None:
        if key < curr.key:
            prev = curr
            curr = curr.left
            left = True

        elif key == curr.key:  # klucz juz jest w drzewie
            return False
        else:
            prev = curr
            curr = curr.right
            left = False

    curr = BSTNode(key)  # tworze klucz
    if left:
        prev.left = curr
    else:
        prev.right = curr

    curr.parent = prev

    return True

def remove(root,key):
    if not find(root,key): #gdy nie ma elementu w drzewie
        return False
    else:
        root = find(root,key)

    if root.left == root.right is None: #gdy element jest lisciem
        root.parent = None
        return True

    elif root.left is None: #sytacja z jednym dzieckiem
        root.right.parent = root.parent
        root.parent = None
        return True
    elif root.right is None: #sytacja z jednym dzieckiem
        root.left.parent = root.parent
        root.parent = None
        return True
    else: #sytacja z dwojgiem dzieci
        copy = find_next(root,key) #szukam nastepnika
        remove(root,copy) #usuwam nastepnik
        root.key = copy
        return True

tree = BSTNode(21)

insert(tree, 15)
insert(tree, 37)
insert(tree, 5)
insert(tree, 20)
insert(tree, 25)
#print(insert(tree,37))
#print(insert(tree,21))
#print(insert(tree,5))
#print(insert(tree,26))
#print(remove(tree,37))

tree1 = BSTNode(10)
insert(tree1, 5)
insert(tree1, 2)
insert(tree1, 4)
insert(tree1, 20)
insert(tree1, 15)
insert(tree1, 12)
insert(tree1, 17)
insert(tree1, 25)
insert(tree1, 22)
insert(tree1, 27)
insert(tree1, 21)
insert(tree1, 24)
print(remove(tree1,2))
print(remove(tree1,17))
print(remove(tree1,20))
print(remove(tree1,20))