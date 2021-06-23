#def left(i):
 #   return


#def right(i):
 #   return 2 * i + 2


def max_heapify(A, i, heap_size):
    l = 2 * i + 1
    r = 2 * i + 2
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)


def build_max_heap(A):
    heap_size = len(A)
    for i in range(heap_size // 2 - 1, -1, -1):
        max_heapify(A, i, heap_size)


def heap_sort(A, heap_size):
    build_max_heap(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, 0, heap_size)

    return A


A = [15, 13, 9, 10, 2, -1, 11, 30]
#test.test_sort(heap_sort, 10, 100, (-1000, 1000), True)
#print(heap_sort(A,len(A)))

def add_to_max_heap(A, val):
  A.append(val)
  n = len(A)
  i = n - 1
  pi = (i-1)//2 # pi - parent index

  while pi >= 0:
    max_heapify(A, n, pi)
    pi = (pi-1)//2


add_to_max_heap(A,14)
print(A)

print(heap_sort(A,len(A)))