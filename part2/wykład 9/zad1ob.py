def remove(G):
    n = len(G)
    visited = [False]*n
    parents = [None]*n
    entry = [0]*n #czas wejscia
    process = [0]*n #czas przetworzenia
    time = 0

    def dfs_visit(u):
        nonlocal G, visited,time
        time += 1
        visited[u] = True
        entry[u] = time
        for i in range(n): #jesli jest implementacja macierzowa trzeba zmienic petle
            if not visited[i] and G[u][i]:
                parents[i] = u
                dfs_visit(i)
        time += 1
        process[u] = time

    for v in range(n):
        if not visited[v]:
            dfs_visit(v)

    for i in range(n): #krotka z indeksem i czasem przetworzenia
        process[i] = (process[i],i)

    process = sorted(process, key = lambda x: x[0]) #sortuej po czasie przetowrzenia

    for i in range(n):
        process[i] = process[i][1]

    for i in range(n): #usuwam krawedzie z wierzchołków od najmniejszego czasu przetworznia
        for j in range(n):
            G[i][j] = 0

    return process

#G = [[0,1,1,0],[1,1,0,0],[1,1,0,1],[0,0,1,0]]
#G = [[0, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1], [0, 0, 0, 1, 1, 0]]
#G = [[0, 1, 0, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1, 1, 0], [0, 1, 0, 1, 0, 1, 1, 0], [0, 0, 1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0]]
print(remove(G))