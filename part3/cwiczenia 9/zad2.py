#tworzymy silne spójne składowe
#w obrębie każdej silnej składowej możemy stworzyć ścieżkę po każdym wierzchołku który do niej należy
#algorytm silnych spojnych składowych ma tę właność, że pierwsza odcięta spójna składowa będzie na początku sortowania topologicznego
#względem innych silnych składowych
#wystarczy wybrać jakikolwiek wierzchołek z pierwszej odcietej silnej składowej, on będzie na początku po posortowaniu topologicznym
#więc będzie istniejc od niego ścieżka w obrębie swojej spójnej składowej do innych wierzchołków i nastpęnych składowych
#nalezy raz póścić DFSa, żeby upewnić się, że z pierwszej spójnej składowej da się przedostać do pozostalych
#zlożoność ssp to O(ElogV)

def swap_graph(G): #funkcja odwraca kolejnosc krawedzi w reprezentacji listowej
    n = len(G)
    new_G = [[] for _ in range(n)]
    for i in range(n):
        for j in range(len(G[i])):
            new_G[G[i][j]].append(i)

    return new_G

def DFS(G): #implementacja dla list sasiedztwa, zakładam ze indeksuje od 0
    n = len(G)
    visited = [False]*n
    process = [0]*n #czas przetworzenia
    time = 0

    def dfs_visit(u):
        nonlocal G, visited,time
        time += 1
        visited[u] = True
        for v in G[u]:
            if not visited[v]: #v - 1 gdy indeksuje od 0, lub v gdy od 1
                dfs_visit(v)
        time += 1
        process[u] = time

    for v in range(n): #zaczynam z kazdego wierzcholka
        if not visited[v]:
            dfs_visit(v)


    return process

def DFSv2(G,s):
    n = len(G)
    visited = [False]*n

    def dfs_visit(u):
        nonlocal G, visited
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(v)

    dfs_visit(s)

    return visited


#dzieki odwroceniu krawedzi i posortowaniu po czasie przetworzenia malejaco zamkniemy spójne składowe tak aby jedno wywoałanie dfs przebiegło dokładnie po jednej składowej
def SPS(G): #silnie spójne składowe
    n = len(G)
    process = DFS(G)
    G = swap_graph(G) #odwracam krawedzie

    for i in range(n):
        process[i] = (i,process[i]) #krotka trzyma mi indeks i czas

    process = sorted(process, key=lambda x: x[1],reverse=True) #sortuje po czasach przetowrzenia malejaco

    visited = [False]*n
    component = [0]*n
    ind = 0

    def dfs_visit(u):
        nonlocal G, visited
        visited[u] = True
        component[u] = ind
        for v in G[u]:
            if not visited[v]:
                dfs_visit(v)
                component[v] = ind #ustawiam ta sama wartosc w jednej skladowej

    for i in range(n):
        if not visited[process[i][0]]: #odpalam dfsa malejaco po czasach przetworzenia, kazdy kolejny dfs odpali sie dla nowej skladowej
            dfs_visit(process[i][0])
            ind += 1 #dla nastepnej silnej skladowej nowa wartosc


    return component #te same wartosci symbolizuja ta sama spojna skladowa

def good_start(G):
    component = SPS(G)
    n = len(component)

    potential_v = None
    for i in range(n):
        if component[i] == 0:
            potential_v = i
            break

    visited = DFSv2(G,potential_v)

    for i in range(n):
        if not visited[i]:
            return False
    return True, potential_v


G = [[1,4],[2,3],[0,7],[4,6],[5],[3],[5],[9],[7,6],[10],[8,5]] #True,np 0
print(good_start(G))

G = [[1],[2,4],[3],[0],[5],[6],[7],[4]] #True,np 0
print(good_start(G))

G = [[2],[2],[]]
print(good_start(G)) #False
