#rozwiazanie Pawla G
def HoraePartition(T, l, r):
    mid = (l + r) // 2 #piwot na srodku, moze byc na koncu lub poczatku
    pivot = T[mid]
    i = l - 1
    j = r + 1
    while True:
        i += 1
        while (T[i] < pivot):
            i += 1

        j -= 1
        while (T[j] > pivot):
            j -= 1

        if (i >= j):
            return j

        T[i], T[j] = T[j], T[i]


def quicksort(T, l, r):  # Standard algo
    if l < r:
        q = HoraePartition(T, l, r)
        quicksort(T, l, q)
        quicksort(T, q + 1, r)


'''rozwiazanie z neta
function AlgHoara(A[1..n],k); 
begin 
  if n=1 and k=1 then return A[1]; 
  // Partition 
  m:=A[1]; l:=1; r:=n; 
  while(l<r) do begin 
    while (A[l]<m) do l++; 
    while (m<A[r]) do r--; 
    if (l <=r) then begin 
      tmp:=A[l]; A[l]:=A[r]; A[r]:=tmp; 
      l++; r--; 
    end; 
  end; 
  if (k<=r) then 
    return AlgHoara(A[1..r],k) 
  else 
    return AlgHoara(A[r+1..n],k-r) 18 
end;'''