#łatwiej zrobić to grafowo
#f(i,j) - czy da sie skleić odcinki wykorzystują do itego, zajumując j, gdzie j jest od a do b
#F[i][j] = F[i][j] or F[k][j - (T[i][1] - T[i][0])]

def sticking(T, a, b):
    n = len(T)
    last = None
    F = [[0]*(b - a + 1) for _ in range(n)]
    T.sort(key=lambda x: x[0])

    for i in range(n):
        if T[i][0] == a:
            F[i][T[i][1] - T[i][0]] = 1
            last = i

    if last is None:
        return False

    for i in range(last,n):
        for j in range(b - a + 1):
            for k in range(i):
                if a + j == T[i][1]:
                    F[i][j] = F[i][j] or F[k][j - (T[i][1] - T[i][0])]


    for i in range(n):
        if F[i][b - a]:
            return True

    return False

T = [[4,6],[7,9],[3,4],[6,8],[9,10],[4,7],[8,10]]
a = 3
b = 10
#print(sticking(T,a,b)) #True
a = 2
b = 10
#print(sticking(T,a,b))
T = [[4,6],[7,9],[2,4],[6,8],[9,10],[4,7]] #False
a = 3
b = 9
#print(sticking(T,a,b)) #False
A = [[0, 3], [3, 7], [3,4], [-2, 0]]
a = 0
b = 7
print(sticking(A,a,b)) #True