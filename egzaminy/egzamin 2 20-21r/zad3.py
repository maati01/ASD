from zad3testy import runtests


# tworze tablice dla lampek
# przełączam lampki z zakresu itej operacji
# sprawdzam obecny stan niebieskich lampek
# aktualizuje rozwiązanie
# O(n + T)

def lamps(n, T):
    result = 0
    temp_res = 0
    lamps = [0] * n  # 0 zielony, 1 czerwony, 2 niebieski

    for i in range(len(T)):
        for j in range(T[i][0], T[i][1] + 1):
            if lamps[j] == 0:
                lamps[j] = 1
            elif lamps[j] == 1:
                lamps[j] = 2
                temp_res += 1
            elif lamps[j] == 2:
                lamps[j] = 0
                temp_res = max(temp_res - 1, 0)

        if temp_res > result:
            result = temp_res

    return result


runtests(lamps)
