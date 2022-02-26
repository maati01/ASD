#jeśli w zasięgu jest tańsza stacja to tankuje tylko tyle żeby do niej dojechać
#jeśli ta na której jestem jest najtańsza w zasiegu to tankuje do pełna
#zakładam że startuje z pełnym bakiem
def tank_with_costs(B,stations,costs,l):
    n = len(stations)
    ind = 0 #indeks dla nastepnych stacji
    i = 0 #pozycja na jakiej stacji jestem
    next_station = stations[0]
    cost = 0
    temp_l = l
    smallest_cost = costs[0]
    smallest_ind = 0
    cnt = 0
    fuel = l - stations[0]
    result = []

    if l < stations[0]:
        return False

    while stations[i] + fuel < B:
        while next_station - stations[i] <= l:
            if costs[ind] < smallest_cost:
                smallest_cost = costs[ind]
                smallest_ind = ind

            if ind + 1 < n: #gdy jest nastepna stacja
                temp_l -= next_station - stations[i]
                next_station = stations[ind+1]
                ind += 1
            else:
                break

        if i == smallest_ind: #w poblizu nie ma tanszej stacji
            if B - stations[i] > l:
                cnt += 1
                cost += (l - fuel)*costs[i]
            else: #gdy moge jednym najtanszym tankowanie dojechać do konca
                cost += ((B - stations[i]) - fuel)*costs[i]
                cnt += 1
            result.append(stations[i])

            if i + 1 >= n: #sytacja gdy jestem na ostaniej stacji i muszę zatankować
                if B - stations[i] > l: return False
                else: return cost, cnt, result

            fuel = l - (stations[i + 1] - stations[i])
            i += 1
            smallest_cost = costs[i]
            smallest_ind = i
            temp_l = l

        else:
            if stations[smallest_ind] - stations[i] > fuel: #gdy nie mam wystarczajaco paliwa zeby dotrzec do najtanszej stacji, tankuje żeby tylko dojechać
                cost += ((stations[smallest_ind] - stations[i]) - fuel)*costs[i]
                fuel = 0
                cnt += 1
                result.append(stations[i])
            else:
                fuel -= stations[smallest_ind] - stations[i]

            ind = smallest_ind
            i = smallest_ind
            next_station = stations[i]
            temp_l = l

        if ind == n - 1 and B - stations[ind] > l: return False #gdy nie moge dojechac do konca z ostatniej stacji
        if next_station - stations[i] > l: return False #gdy dwie stacjie są za daleko od siebie

    return cost, cnt, result

stations = [2,3,6]
costs = [4,3,3]
B = 9
l = 3
print(tank_with_costs(B,stations,costs,l)) #(18, 2, [3, 6])

stations = [2, 7, 12, 15, 20]
costs = [4, 3, 10, 1, 4]
B = 23
l = 10
print(tank_with_costs(B,stations,costs,l)) #(23, 2, [7, 15])

stations = [2,4,8,9,15,18]
costs = [1,1,1,1,1,2]
B = 20
l = 19
print(tank_with_costs(B,stations,costs,l)) #(1, 1, [2])

stations = [2,4,8,9,15,18]
costs = [1,1,1,1,1,2]
B = 20
l = 4
print(tank_with_costs(B,stations,costs,l)) #False

stations = [2,4,8,9,13,15,18]
costs = [1,1,1,1,1,1,2]
B = 20
l = 4
print(tank_with_costs(B,stations,costs,l)) #(17, 7, [2, 4, 8, 9, 13, 15, 18])