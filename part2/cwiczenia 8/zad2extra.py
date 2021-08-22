#jeśli mogę zmieniać reprezentację to tworzę graf w postaci macierzy i w czasie O(v^2)
#jeśli muszę zachować reprezentację grafu to sortuje krawedzie dla kazdego wierzchołka
#szukam binary searchem czy występuje krawędź w drugą stronę O(ElogV)

def binary_search(arr, x):
    left, right = 0, len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if x == arr[mid]:
            return 1

        elif x < arr[mid]:
            right = mid - 1

        else:
            left = mid + 1

    return 0

def directed(G):
    n = len(G)
    for i in range(n):
        G[i].sort()

    for i in range(n):
        for j in range(len(G[i])):
            if not binary_search(G[G[i][j]],i):
                return False
    return True

# True
graph = [[1, 3],
         [0, 2],
         [1, 3],
         [0, 2]]
print(directed(graph))

# False
graph = [[1],
         [2],
         [3],
         [0]]
print(directed(graph))
