#najbardziej skrajny punkt od lewej jest poczatkiem nowego przedziału i rozszerzam go maksymalnie
#zaczynam od nowego skrajnego punktu nowy przedział

def compartments(A):
    n = len(A)
    result = []
    start = A[0]

    i = 0
    while i < n:
        if A[i] > start + 1:
            result.append([start,start + 1])
            start = A[i]

        i += 1

    result.append([start, start + 1])

    return len(result), result





A = [0.25,0.5,1.6]
print(compartments(A))
A = [0.25,0.5,1.25]
print(compartments(A))
A = [0.25,0.5,1.6,1.8,2]
print(compartments(A))
A = [0.25,0.5,1.6,1.8,2,3]
print(compartments(A))
