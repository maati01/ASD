class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

def add(root, key):
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

        # elif key == curr.key: #klucz juz jest w drzewie
        # return False

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

    # return True #w zależności od implementacji
    return root

def find(root, key):
    while root != None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right

    return None