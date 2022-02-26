#f(v) - wartość najlepszej ścieżki zaczynającej się na wierzchołku v i kierującej się w stronę liści
#f(i) = max(0, v.val, v.val + f(left), v.val + f(right))
#result: max(v.val + f(left) + f(right))
#funkcja od prof. Faliszewskiego z dodanym brakujacym warunkiem

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.f = 0 #nieobliczona wartosc funkcji
        self.end = 0 #wartość ścieżki połączonej w lewym i prawym poddrzewie, nie możemy kontynuować więc kończymy

def best_path_tree(v): #funkcja zwraca krotke z wartoscią i najlepszym poddrzewem
    if v == None: return (0,0)
    L, best_L = best_path_tree(v.left)
    R, best_R = best_path_tree(v.right)

    v.f = max(0, v.value, v.value + L, v.value + R)

    if v.value + L + R > v.f: #sytacja gdy laczymy sciezke z lewego i prawego poddrzewa w wierzchołku którym jesteśmy
        v.end = v.value + L + R

    best = max(best_L, best_R, v.f, v.end)

    return v.f, best


#test prowizoryczny, nie zwracać uwagi XD
root = Node(10)
a = Node(7)
b = Node(-5)
c = Node(8)
d = Node(-100)
e = Node(2)
f = Node(1)
g = Node(-7)
h = Node(20)
i = Node(7)
j = Node(-5)
k = Node(1)
l = Node(-4)
root.left = a
root.right = b
a.left = c
b.left = d
b.right = e
c.left = f
c.right = g
g.right = k
f.left = j
j.left = l
e.left = h
e.right = i

print(best_path_tree(root))