#sprawdzam dla kazdego wierzchołka v czy jest skierowany do jakiegoś innego
#z każdego innego sprawdzam czy ma połączenie do v
#O(n^2)

def universal_output(G):
    n = len(G)

    for i in range(n):
        flag = True
        for j in range(n):
            if (G[i][j] == 1 or G[j][i] == 0) and i != j:
                flag = False
                break
        if flag:
            return i

    return False


# 0
graph = [[0, 0, 0, 0],
         [1, 0, 0, 0],
         [1, 0, 0, 0],
         [1, 0, 1, 0]]
print(universal_output(graph))
# None
graph = [[0, 0, 0, 0, 0],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 1, 0, 1],
         [0, 0, 0, 0, 0]]
print(universal_output(graph))
# 4
graph = [[0, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 1, 0, 1],
         [0, 0, 0, 0, 0]]
print(universal_output(graph))