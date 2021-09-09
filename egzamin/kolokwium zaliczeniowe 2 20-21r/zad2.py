from zad2testy import runtests

#O(N + M)
#tworze graf w postaci krawędziowej gdzie spełniony jest warunek A%10**K == B//10**K
#szukam potencjalnego końca i początku w ścieżce Eulera
#tworzę miedzy nimi tymczasową krawędź, aby znaleźć cykl Eulera
#szukam cyklu za pomocą hierholzers_algorithm
#w miejscu tymczasowej krawedzi obcinam cykl
#sklejam w taki sposób aby powstała ścieżka

def hierholzers_algorithm(G,start): #cykl dla DAGa
    curr_path = [start]
    circuit = []

    while curr_path:
        curr_v = curr_path[-1]

        if G[curr_v]:
            next_v = G[curr_v].pop()
            curr_path.append(next_v)
        else:
            circuit.append(curr_path.pop())

    return circuit[::-1]

def check_bad_edge(path,start,end):
    for i in range(len(path)):
        if path[i] == end and path[i+1] == start:
            return i + 1

def get_result(path,bad,K):
    result = []

    for i in range(bad,len(path) - 1):
        result.append(path[i]*10**K + path[i+1])
    for i in range(0,bad - 1):
        result.append(path[i] * 10 ** K + path[i + 1])

    return result

def order(L,K):
    n = len(L)
    m = 10**K
    graph = [[] for _ in range(m)]
    counter = [[0,0] for _ in range(m)] #in, out

    for i in range(n):
        graph[L[i]//10**K].append(L[i]%10**K)

    for i in range(m):
        for j in range(len(graph[i])):
            counter[graph[i][j]][0] += 1
            counter[i][1] += 1

    start = None
    end = None
    for i in range(m):
        if counter[i][0] == counter[i][1] + 1:
            if end is not None: return None
            end = i

        if counter[i][1] == counter[i][0] + 1:
            if start is not None: return None
            start = i

    graph[end].append(start)

    path = hierholzers_algorithm(graph,start)

    bad_ind = check_bad_edge(path,start,end)

    return get_result(path,bad_ind,K)

runtests( order )
