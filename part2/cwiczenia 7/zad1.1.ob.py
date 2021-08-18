def tank(B,T,l):
    cnt = 0
    n = len(T)
    i = 0
    next_station = T[0]
    ind = 0
    temp_l = l
    result = []

    if T[0] > l:
        return False

    while i + temp_l < B:
        if temp_l + i >= next_station:
            temp_l -= next_station - i
            i = next_station
            if ind + 1 < n:
                next_station = T[ind + 1]
                ind += 1
            elif ind + 1 >= n and i + l < B:
                return False
            else:
                result.append(i)
                return cnt+1, result
        elif l + i < next_station:
            return False
        else:
            result.append(i)
            cnt += 1
            temp_l = l

    return cnt, result



l = 5
T = [2,5,7,9,11]
B = 13
print(tank(B,T,l)) #(2, [5, 9])

l = 5
T = [2,5,7,9,11]
B = 15
print(tank(B,T,l)) #(3, [5, 9, 11])

l = 4
T = [2,5,7,9,11]
B = 15
print(tank(B,T,l)) #(4, [2, 5, 9, 11])

l = 4
T = [2,5,7,9,11]
B = 16
print(tank(B,T,l)) #False

l = 2
T = [2,5,7,9,11]
B = 13
print(tank(B,T,l)) #False

l = 3
T = [2,5,7,9,11]
B = 13
print(tank(B,T,l)) #(5, [2, 5, 7, 9, 11])