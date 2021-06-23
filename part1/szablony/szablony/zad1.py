from zad1testy import runtests
#Mateusz Powęska
#funkcja przerabia tablice dwuwymiarową w czasie O(n^2) wykorzystując n^2 pamięci
#uzywam selecta z wykorzystanie partitiona w czasie nlogn dzieki czemu wiem jakie beda przekątne
#przepisuje przekątne do wyjściowej tablicy w czasie n^2 dzieki czemu mam orientacje jak przestawic elementy
#w czsie 2*n^2 przepisuje elementy nad i pod przekątną
#uwzględniająć że wykonuje kilka razy operacje kwadratową której czas jest większy od quickselecta czas będzie O(n^2), a pamięć dodatkowa będzie wynosić n^2
def partation(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def select(A,a,b,i):
    if a == b:
        return A[a]

    q = partation(A,a,b)

    if i == q: #wynikiem jest element rodzielający
        return A[q]

    elif i < q:
        return select(A,a,b - 1,i)

    else:
        return select(A,a+1,b,i) #(k-i)

def Median(T):
    n = len(T)
    tab = [0]*(n*n)
    k = 0
    for i in range(n): #przerabiam tablice dwuwymiarową na jednowymiarową
        for j in range(n):
            tab[k] = T[i][j]
            k += 1


    if (n*n)%2 != 0: #indeks dla tablicy nieparzystej
        p = select(tab, 0, n * n - 1,((n*n)//2) - (n//2))  # wyznaczam indeksy dla przekątnej
        q = select(tab, 0, n * n - 1,((n*n)//2) + (n//2))
    else: #indeks dla tablicy parzystej
        p = select(tab, 0, n * n - 1,((n*n)//2) - (n//2))  # wyznaczam indeksy dla przekątnej
        q = select(tab, 0, n * n - 1,((n*n)//2) + (n//2) - 1)


    k = 0
    for i in range(n*n): #umieszczenie przekątnej ze znalezionych wartości
        if tab[i] >= p and tab[i] <= q:
            T[k][k] = tab[i]
            k += 1

    k = 1 #indeksy dla orientacji wzgledem przekątnej
    x = 0
    i = 0
    while i < n*n: #uzupełniam wyjściową tablice elementami wiekszymi od przekątnej
        if tab[i] > q:
            while x < n and k < n:
                T[x][k] = tab[i] #nadpisanie odpowiedniej wartosci do wyjsciowej tablicy
                k += 1
                i += 1
            x += 1
            k = x + 1
        else:
            i += 1


    i = 0 #indeksy dla orientacji wzgledem przekątnej
    a = 0
    b = 1
    row = 1
    while i < n*n: #uzupełniam wyjściową tablice elementami mniejszymi od przekątnej
        if tab[i] < p:
            while a < row:
                T[b][a] = tab[i] #nadpisanie odpowiedniej wartosci do wyjsciowej tablicy
                a += 1
                i += 1
            a = 0
            row += 1
            b += 1
        i += 1

    return T


runtests( Median )
