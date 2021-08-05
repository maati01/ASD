def anagram(A,B):
    n = len(A)
    m = len(B)

    if n != m:
        return False

    max_val = ord(A[0])

    for i in range(1,n):
        if max_val < ord(A[i]):
            max_val = ord(A[i])

    counters = [0]*(max_val + 1)

    for i in range(n):
        counters[ord(A[i])] += 1

    for i in range(n):
        counters[ord(B[i])] -= 1
        if counters[ord(B[i])] < 0:
            return False

    return True


A = 'AbcdEf'
B = 'bAdcfE'
C = 'AbcdrEf'
D = 'AbcdREf'

print(anagram(A,B))
print(anagram(C,D))