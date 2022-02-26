def insertion_sort(arr,left,right): #insertion sort sluzy do posortowania "piątek", mała ilość gwarantuje liniowy czas, zmodyfikowany tak aby sortował okreslony fragment tablicy
  for i in range(left+1, right+1):
    key = arr[i]
    j = i - 1

    while j >= left and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1

    arr[j + 1] = key

  return arr

def get_median(left,right): #funkcja pozwala wyznaczyć indeks mediany
    return (left + right)//2 #biorę mniejsza mediane gdy jest parzysta ilosc

def partation(A,left,right,x): #funkcja partation taka jak w quicksortcie, ale szuka indeks dla mediany i zamienia ją z ostanim elementem
    for i in range(left, right):
        if A[i] == x:
            A[right],A[i] = A[i],A[right]
            break
    x = A[right]
    i = left - 1
    for j in range(left, right):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[right] = A[right], A[i + 1]
    return i + 1


def linearselect(A, left, right,k):
    if (k >= left and k <= right): #warunek końca pętli
        n = len(A)
        indeks = 0
        rest = n%5 #gwarancja stworzenia ciagów o dlugosci 5, ewentualny ciąg < 3 rozpatrze osobno
        for i in range(0,n-rest,5): #PROBLEM PRAWDOPODOBNIE Z KROKAMI O 5 DLA TABLIC < 15
            insertion_sort(A,i,i+4) #sortuje podciągu długosci 5
            A[left + indeks],A[get_median(left,right)] = A[get_median(left,right)],A[left + indeks] #zamieniam mediany w kolejnych piątkach z początkowymi indeksami w tablicy aby je przechowywac i nie tworzyć dodatkowej tablicy
            indeks += 1

        if rest != 0: #sortuje ewentualny podciag <5
            insertion_sort(A,i+4,i + 4 + rest)
            A[indeks], A[get_median(i,i+4)] = A[get_median(i,i+4)], A[indeks]
            indeks += 1

        if indeks == 1:
            medOfMed = A[left]
        else:
            medOfMed = linearselect(A, left, left + indeks - 1, indeks//2) #wywołanie rekurencyjne aby wyznaczyć medianę median

        pos = partation(A, left, right, medOfMed) #pozycja piwota

        if (pos == k):
            return A[pos]

        if (pos > k):
            return linearselect(A, left, pos - 1, k)

        return linearselect(A, pos + 1, right,k)

    return 10**100

