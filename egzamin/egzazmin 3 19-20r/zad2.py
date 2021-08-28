from zad2testy import runtests

#dynamicznie
#opis jest w rozwiazaniu z zestawów

def tower(A):
  n = len(A)
  F = [1]*n

  for i in range(n):
    for j in range(i):
      if A[i][0] >= A[j][0] and A[i][1] <= A[j][1]:
        F[i] = max(F[i],F[j] + 1)

  return max(F)

runtests( tower )
