# binary search tree

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


def prev(root, key):
    root = find(root, key)
    if root is None:
        return None
    elif root.left is None:  # sytacja gdy nie moge isc w lewo
        if root.parent is None:  # sytacja z samym rootem
            return root
        else:  # wspinam sie po lewej az raz przejde po prawej
            while root.key < root.parent.key:
                root = root.parent
                if root.parent is None:  # sytacja gdy nie ma poprzednika
                    return None
            return root.parent.key

    root = root.left

    while root.right != None:  # sytuacja gdy moge pojsc raz w lewo doł a potem maksimum w prawo
        root = root.right

    return root.key


def find_next(root, key):
    root = find(root, key)
    if root is None:
        return None
    elif root.right is None:  # sytacja gdy nie moge isc w prawo
        if root.parent is None:  # sytacja gdy mamy samego roota
            return root.key
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


def display(self):
    lines, *_ = display_aux(self)
    for line in lines:
        print(line)


def display_aux(self):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if self.right is None and self.left is None:
        line = '%s' % self.key
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if self.right is None:
        lines, n, p, x = display_aux(self.left)
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if self.left is None:
        lines, n, p, x = display_aux(self.right)
        s = '%s' % self.key
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = display_aux(self.left)
    right, m, q, y = display_aux(self.right)
    s = '%s' % self.key
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2

def remove(tree,key):
    root = find(tree,key)
    if root is None:
        return tree

    if root.right is None and root.left is None: #sytacja z liściem
        if root.parent.key > root.key:
            root.parent.left = None

        else:
            root.parent.right = None

    elif root.left is None: #sytacja z jednym dzieckiem
        if root.parent.key > root.right.key:
            root.right.parent = root.parent
            root.parent.left = root.right

        else:
            root.right.parent = root.parent
            root.parent.right = root.right


    elif root.right is None: #sytacja z jednym dzieckiem
        if root.parent.key > root.left.key:
            root.left.parent = root.parent
            root.parent.left = root.left

        else:
            root.left.parent = root.parent
            root.parent.right = root.left

    else: #gdy mam dwoje dzieci, szukam nastepnika, usuwam go a jego wartosc nadpisuje w miejsce które chcialem pierwotnie usunąć
        next_val = find_next(tree,key)
        tree = remove(tree,next_val)
        root.key = next_val

    return tree

def array_to_bst(A):
  if len(A) == 0:
    return None

  tree = BSTNode(A[0])

  for i in range(1, len(A)):
    tree = add(tree, A[i])

  return tree

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
print(prev(tree,13))
print(find_next(tree,20))
print(find_next(tree,13))
display(tree)
tree = remove(tree,37)
display(tree)

tree = remove(tree,25)
display(tree)
tree = remove(tree,15)
display(tree)
tree = remove(tree,13)
display(tree)