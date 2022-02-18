#tym razem dynamicznie
#w sumie nie wiem czy zachłan zadziała
#f(i,j) - minimalny koszt gdy do itej stacji włącznie z tankowaniem na itej mając j paliwa
#f(i,j) = min(f(k) + cost[i]), gdzie k jest od 0 do i

from math import inf

def tank_dp(B,stations,costs,l):
    n = len(stations)
    F = [inf]*(n)
    F[0] = 0

    for i in range(n):
        for k in range(i,n):
            if stations[k] - stations[i] <= l:
                F[k] = min(F[i] + l*costs[i],F[k])

    result = inf
    for i in range(n):
        if B - stations[i] <= l and F[i] < result:
            result = F[i+1]

    return result


stations = [2, 7, 12, 15, 20]
costs = [4, 3, 10, 1, 4]
l = 10
B = 23
print(tank_dp(B,stations,costs,l))# (29, [0, 7, 15, 23]

stations = [2, 3, 6]
costs = [4, 3, 3]
l = 3
B = 9
print(tank_dp(B,stations,costs,l))# (18, [0, 3, 6, 9])

stations = [2, 4, 8, 9, 15, 18]
costs = [1, 1, 1, 1, 1, 2]
l = 19
B = 20
print(tank_dp(B,stations,costs,l))# (2, [0, 2, 20])

stations = [2, 4, 8, 9, 15, 18]
costs = [1, 1, 1, 1, 1, 2]
l = 4
B = 20
print(tank_dp(B,stations,costs,l)) # (-1, None)