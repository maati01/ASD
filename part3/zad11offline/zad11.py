class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

def find(root,key):
    while root != None:
        if root.key == key:
            return True
        elif key < root.key:
            root = root.left
        else:
            root = root.right

    return False


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



tree = BSTNode(21)

insert(tree, 15)
insert(tree, 37)
insert(tree, 5)
insert(tree, 20)
insert(tree, 25)
print(insert(tree,37))
print(insert(tree,21))
print(insert(tree,5))
print(insert(tree,26))

