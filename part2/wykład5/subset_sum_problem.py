# f(i,j) = f(i-1,j) or f(i-1,j-A[i-1])

#Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

# A Dynamic Programming solution for subset

def isSubsetSum(set, sum):
    #wartosc w subset[i][j] wskazuje rozwiazanie
    n = len(set)
    subset = ([[False for i in range(sum + 1)] #tablica dwywymiarowa wartosci false
               for i in range(n + 1)])

    for i in range(n + 1): #pierwsza kolumna ma wartosci true(dla sumy 0)
        subset[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, sum + 1): #dla kazdej wartosci iteruje po mozliwych sumach 0...sum
            if j < set[i - 1]:
                subset[i][j] = subset[i - 1][j]  #jesli suma juz wystepuje to zawsze bedzie true, jesli jest mniejsza od wartosci i nie wystapila = false
            if j >= set[i - 1]:
                subset[i][j] = (subset[i - 1][j] or subset[i - 1][j - set[i - 1]]) #sprawdzan czy suma juz wystapila lub czy wystapiła suma ktora jest roznica obecnej i poprzedniej
    return subset[n][sum] #ostatnia komórka zwraca rozwiazanie


print(isSubsetSum([2,4,3,1,6],5))