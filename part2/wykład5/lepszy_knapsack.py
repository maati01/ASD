from math import inf


def knapsack2(P, W, max_w):
    max_p = sum(P)
    n = len(W)
    if n == 0:
        return (None, 0, max_p)

    # tworzymy tablice, w ktorej:
    # wiersze - do ktorego przedmiotu juz rozwazylismy
    # kolumny - jaki profit mamy miec conajmniej
    # wartosc pola - minimalna waga dla danego profitu lub wiekszego
    F = [None] * n  # O(n)
    for i in range(n):  # O(n)
        F[i] = [inf] * (max_p + 1)

    # dla profitu 0 nie bierzemy zadnego przedmiotu
    for i in range(n):  # O(n)
        F[i][0] = 0

    # dla pierwszego rzedu problem jest trywialny
    for p in range(1, P[0] + 1):  # O(max_p+1-W[0]) <= O(max_p)
        F[0][p] = W[0]

    for i in range(1, n):  # O(n)
        for p in range(1, max_p + 1):  # O(max_p)
            # ustawiamy wage minimalna taka jak dla i-1 elementow
            F[i][p] = F[i - 1][p]

            # jezeli aktualnie rozwazany profit jest mniejszy badz rowny aktualnemu zyskowi z elementu to
            # bierzemy minimalną wartość z aktualnego F[i][p] oraz z wagi aktualnego elementu
            # nie dobieramy elementu albo b ierzemy tylko i-ty element
            if p <= P[i]:
                F[i][p] = min(F[i][p], W[i])
            # jezeli aktualnie rozwazany profit jest wiekszy od aktualnego zysku z elementu to
            # bierzemy min z aktualnej wagi + wage z profitu p-P[i] dla i-1 elementow oraz z aktualnej wartosci
            # nie dobieramy elementu albo dodajemy i-ty element
            else:
                F[i][p] = min(F[i][p], F[i - 1][p - P[i]] + W[i])

    # szukamy maksymalnego mozliwego zysku idac od maks zysku
    # jezeli waga sie zgadza to znalezlismy rozwiazanie


    for p in range(max_p, -1, -1):
        if F[n - 1][p] <= max_w:
            return (F, p, max_p)


    return (None, 0, max_p)


def get_solution2(F, P, W, i, p):
    # jezeli rozpatrzylismy wszystkie elementy poza ostatnim
    if i == 0:
        # jezeli profit nam na to pozwala to bierzemy element
        if p >= P[0]: return [0]
        return []

    # jezeli profit nam pozwala na wziecie elementu
    # i wyglada jakbysmy go mieli wziac
    # lub bedzie to ostatni element, ktory mamy wziac
    # to go bierzemy
    if p >= P[i] and (F[i][p] == F[i - 1][p - P[i]] + W[i] or F[i][p] == W[i]):
        return get_solution2(F, P, W, i - 1, p - P[i]) + [i]
    return get_solution2(F, P, W, i - 1, p)


W = [4, 5, 12, 9, 10, 13, 5, 8, 7, 3, 6, 13, 23, 5, 34, 23, 12]
P = [10, 2, 4, 5, 3, 4, 8, 4, 2, 10, 4, 10, 12, 4, 16, 19, 4]
max_w = 40
F,res,max_p = knapsack2(P, W, max_w)
print(get_solution2(F,P,W,len(W)-1,res))