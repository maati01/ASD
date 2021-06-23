#binary search tree

class BSTNode:
    def __init__(self,key):
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

    return None


'''def add(root, key): #dodawanie rekurencyjne

    if root is None:
        root = BSTNode(key)
    elif key < root.key:
        print(root.key)
        root.left = add(root.left, key)
    elif key > root.key:
        print(root.key)
        root.right = add(root.right, key)

    return root'''

def add(root,key):
    curr = root
    prev = None
    if curr is None:
        root = BSTNode(key)
        return root

    while curr is not None:
        if key < curr.key:
            prev = curr
            curr = curr.left
            left = True

        #elif key == curr.key: #klucz juz jest w drzewie
            #return False

        else:
            prev = curr
            curr = curr.right
            left = False

    curr = BSTNode(key) #tworze klucz
    if left:
        prev.left = curr
    else:
        prev.right = curr

    curr.parent = prev

    #return True #w zależności od implementacji
    return root


def printChildrenFirst(tree: BSTNode):
    if tree is None:
        print("Drzewo puste")
        return
    children = [tree]
    while children:
        newchildren = []
        for i in children:
            print(i.key, end=" ")
            if i.left is not None:
                newchildren.append(i.left)
            if i.right is not None:
                newchildren.append(i.right)
        print("")
        children = newchildren

def min_tree(root):
    if root.left is None:
        return root
    while root.left is not None:
        root = root.left

    return root.key

def max_tree(root):
    if root.right is None:
        return root
    while root.right is not None:
        root = root.right

    return root.key

def prev(root,key):
    root = find(root,key)
    if root is None:
        return None
    elif root.left is None: #sytacja gdy nie moge isc w lewo
        if root.parent is None: #sytacja z samym rootem
            return root
        else: #wspinam sie po lewej az raz przejde po prawej
            while root.key < root.parent.key:
                root = root.parent
                if root.parent is None: #sytacja gdy nie ma poprzednika
                    return None
            return root.parent.key

    root = root.left

    while root.right != None: #sytuacja gdy moge pojsc raz w lewo doł a potem maksimum w prawo
        root = root.right

    return root.key

def find_next(root,key):
    root = find(root, key)
    if root is None:
        return None
    elif root.right is None:#sytacja gdy nie moge isc w prawo
        if root.parent is None: #sytacja gdy mamy samego roota
            return root
        else:
            while root.key > root.parent.key: #ide w góre, aż przejde po wiekszym kluczu
                root = root.parent
                if root.parent is None: #sytacja gdy nie ma nastepnika
                    return None
            return root.parent.key

    root = root.right

    while root.left != None: #sytacja gdy moge isc raz w prawo i ciagle w lewo
        root = root.left

    return root.key

tree = BSTNode(21)

tree = add(tree, 15)
tree = add(tree, 37)

tree = add(tree, 5)
tree = add(tree, 20)
tree = add(tree, 25)

tree = add(tree, 40)
tree = add(tree, 7)
tree = add(tree, 13)
tree = add(tree, 8)

#printChildrenFirst(tree)
#print(prev(tree,40))
#print(find_next(tree,21))

