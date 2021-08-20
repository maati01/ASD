#korzystam z tego, że z potencjalnego uniwersalnego ujścia nie mogą wychodzić krawędzie, a muszą wchodzić
#jeśli warunek nie jest spełniony to zmieniam potencjalne uniwersalne ujście
#dzięki dwóm wskaźniokom złożoność to O(n)

def universal_output(G):
    n = len(G)
    potential_v = 0
    j = 1
    while potential_v < n and j < n:
        if G[potential_v][j] == 1 and G[j][potential_v] == 0:
            potential_v = j
            j += 1
        elif G[potential_v][j] == 0 and G[j][potential_v] == 1:
            j += 1
        else:
            return False

    return potential_v

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

#2
graph = [[0,0,1,1,0],
         [1,0,1,0,1],
         [0,0,0,0,0],
         [0,0,1,0,1],
         [0,0,1,0,0]]
print(universal_output(graph))