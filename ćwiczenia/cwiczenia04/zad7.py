from math import inf
#na potrzeby testów kolory to cyfry od 0 do k - 1
#algorytm przechodzi dwoma indeksami po tablicy wiec wiec O(n)

def all_colors(A, k):
    n = len(A)
    i = 0
    j = 0
    result_i = 0
    result_j = 0
    the_best_result = inf
    colors = [0] * k
    counter = 0

    while j < n:
        while j < n:
            colors[A[j]] += 1
            if colors[A[j]] == 1:
                counter += 1

            if counter == k:
                result = j - i
                if result < the_best_result:
                    the_best_result = result
                    result_i = i
                    result_j = j
                    j += 1
                break

            else:
                j += 1
        while n > j >= i + k - 1:
            colors[A[i]] -= 1
            if colors[A[i]] == 0:
                i += 1
                counter -= 1
                break

            if counter == k:
                i += 1
                result = j - i
                if result < the_best_result:
                    the_best_result = result
                    result_i = i
                    result_j = j



    return the_best_result, result_i, result_j


A = [1,2,0,0,3,3,3,0,2,1]
B = [1,2,0,0,3,1,2,0,0,2]
C = [0,1,2,3,4,5,1]

print(all_colors(A,4))
print(all_colors(B,4))
print(all_colors(C,6))