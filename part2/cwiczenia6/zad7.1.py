#łatwiej zrobić to grafowo
#f(i,j) - czy da sie skleić odcinki wykorzystują do itego, zajumując j, gdzie j jest od a do b
#F[i][j] = F[i][j] or F[k][j - (T[i][1] - T[i][0])]

def sticking(T, a, b):
    n = len(T)
    F = [[0]*(b - a + 1) for _ in range(n)]
    T.sort(key=lambda x: x[0])

    for i in range(n):
        if T[i][0] <= a:
            F[i][T[i][1] - T[i][0]] = 1


    for i in range(1,n):
        for j in range(b - a + 1):
            for k in range(i):
                if j >= T[i][1] - T[i][0]:
                    F[i][j] = F[i][j] or F[k][j - (T[i][1] - T[i][0])]

    for i in range(n):
        if F[i][b - a]:
            return True

    return False

T = [[4,6],[7,9],[3,4],[6,8],[9,10],[4,7]]
a = 3
b = 10
print(sticking(T,a,b))
a = 2
b = 10
print(sticking(T,a,b))
T = [[4,6],[7,9],[2,4],[6,8],[9,10],[4,7]]
a = 3
b = 9
print(sticking(T,a,b))