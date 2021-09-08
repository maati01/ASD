from zad1testy import runtests


def tanagram(x, y, t):
    n = len(x)
    t1 = [0]*n
    t2 = [0]*n
    for i in range(n):
        t1[i] = x[i],i
        t2[i] = y[i],i

    t1.sort(key = lambda x: x[0])
    t2.sort(key = lambda x: x[0])

    for i in range(n):
        if abs(t1[i][1] - t2[i][1]) > t:
            return False

    return True


runtests( tanagram )