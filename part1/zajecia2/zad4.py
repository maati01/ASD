def quick_sort(A,ind):
    p = 0
    r = len(A)-1
    def sub_quick_sort(A,p,r,ind):
        if p < r:
            q = partation(A,p,r,ind)
            sub_quick_sort(A,p,q-1,ind)
            sub_quick_sort(A,p+1,r,ind)

    def partation(A,p,r,ind):
        x = A[r][ind]
        i = p-1
        for j in range(p,r):
            if A[j][ind] <= x:
                i += 1
                A[i],A[j] = A[j],A[i]

        A[i+1],A[r] = A[r],A[i+1]
        return i+1

    sub_quick_sort(A,p,r,ind)
    return A

def water_containers(A,volume):
    n = len(A)
    width = 0
    points = []

    for i in range(n):
        points.append((A[i][0][0],A[i][0][1],1,i)) #0 - bottom of the container
        points.append((A[i][1][0],A[i][1][1],0,i)) #1 - top of the container

    points = quick_sort(points,1)

    n = len(points)
    result = 0
    width = abs(A[points[0][3]][0][0] - A[points[0][3]][1][0])
    last_height = points[0][1]
    for i in range(1,n):
        height_difference = points[i][1] - last_height
        volume -= height_difference*width
        if volume < 0:
            return result
        if points[i][2]:
            result += 1

        if not points[i][2]:
            width += abs(A[points[i][3]][0][0] - A[points[i][3]][1][0])
        else:
            width -= abs(A[points[i][3]][0][0] - A[points[i][3]][1][0])

        last_height = points[i][1]

    return result

A = [[(4,6),(6,4)],[(9,5),(11,3)],[(11,7),(15,6)],[(6,3),(8,2)]]
B = [[(1, -1), (4, -2)], [(1, 2), (2, 0)], [(3, 5), (4, 1)], [(1, 5), (2, 4)], [(-4, 3), (-1, 1)]]
'''print(water_containers(A,1))
print(water_containers(A,2))
print(water_containers(A,3))
print(water_containers(A,4))
print(water_containers(A,5))
print(water_containers(A,6))
print(water_containers(A,10))
print(water_containers(A,14))
print(water_containers(B,1))
print(water_containers(B,2))
print(water_containers(B,3))
print(water_containers(B,4))
print(water_containers(B,5))
print(water_containers(B,6))
print(water_containers(B,10))
print(water_containers(B,14))'''