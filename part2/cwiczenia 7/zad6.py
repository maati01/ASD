#z jakiegoś powodu to mediana XD

def sum_distance(A):
    n = len(A)
    if n % 2 != 0: return A[n//2]
    else: return (A[n//2 - 1] + A[n//2])/2

A = [1,2,100]
B = [1,2,50,100]
print(sum_distance(A))
print(sum_distance(B))