def sum_below(pts, y):
  _sum = 0
  cnt = 0
  for p in pts:
    if p[0][1] <= y:
      _sum += (p[1][0]-p[0][0])*(p[0][1]-p[1][1])
      cnt += 1

  return (_sum, cnt)


P = 10**2
pts = [((1, 10), (3, 8)), ((2, 10), (3, 6))]

y_prev = -1
y = pts[0][0][1]
e = 0.1
while abs(y - y_prev) > e:
  res = sum_below(pts, y)
  if res[0] < P:
    y_prev, y = y, 1.5*y
  else:
    y_prev, y = y, 0.5*y


#wersja darka
def merge(T, A, B):
    index_a = 0
    index_b = 0
    for i in range(len(A) + len(B) - 2):
        if B[index_b][0][1] >= A[index_a][0][1]:
            T[i] = A[index_a]
            index_a += 1
        else:
            T[i] = B[index_b]
            index_b += 1


def max_val(T):
    m = T[0][0][1]
    for x in T:
        if x[0][1] > m:
            m = x[0][1]
    return [[0, m + 1]]


def ms(T, m):
    if len(T) == 1:
        return T

    p = len(T) // 2
    merge(T, ms(T[:p], m) + [m], ms(T[p:], m) + [m])
    return T


def mergesort(T):
    return ms(T, max_val(T))


def pole(p1, p2):
    # print(p2[0] - p1[0])
    # print(p1[1] - p2[1])
    return (p2[0] - p1[0]) * (p1[1] - p2[1])


def solve(T, P):
    mergesort(T)
    i = 0
    for x in T:
        P = P - pole(x[0], x[1])
        if P <= 0:
            break
        i += 1
    print(i)



T = [((1, 10), (3, 7)), ((4, 8), (7, 5)), ((8, 9), (10, 4))]
print(T)
solve(T, 15)