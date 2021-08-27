class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

#tworze BST
#zamiast liczb naturalnych trzymam stringi w węzłach
#tak sprawdzam czy węzeł już występuje, jeśli nie to dodaje go

def find(root, key):
    while root != None:
        if root.key == key:
            return True
        elif key < root.key:
            root = root.left
        else:
            root = root.right

    return False

def add(root, key): #dodawanie rekurencyjne, wuzględniająć liczbę węzłów
    if find(root,key):
        return False

    if root is None:
        root = BSTNode(key)
    elif key < root.key:
        root.left = add(root.left, key)
    elif key > root.key:
        root.right = add(root.right, key)


    return root

def check_different_strings(T):
    n = len(T)

    if n == 0:
        return True

    tree = BSTNode(T[0])

    for i in range(1,n):
        if find(tree,T[i]):
            return False
        else:
            tree = add(tree,T[i])

    return True

test = ['GATC','GAT', 'GAC', 'GG']
print(check_different_strings(test))
test = ['GATC','GAT', 'GAC', 'GG', 'GATC']
print(check_different_strings(test))