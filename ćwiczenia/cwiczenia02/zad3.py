def sum_x(A,x):
    n = len(A)
    i = 0
    j = n - 1
    while i <= j:
        if A[i] + A[j] > x:
            j -= 1
        elif A[i] + A[j] < x:
            i += 1
        elif A[i] + A[j] == x:
            return i, j

    return False

A = [1,3,3,5,6,7,9,9,10,12]
print(sum_x(A,16)) #true
print(sum_x(A,1)) #false
print(sum_x(A,6)) #true
print(sum_x(A,18)) #true
print(sum_x(A,22)) #true
print(sum_x(A,23)) #false