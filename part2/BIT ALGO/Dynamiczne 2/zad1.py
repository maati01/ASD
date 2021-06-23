'''
sum(i,j) - suma liczb od ni do nj, możemy ją obliczać w O(1) jeśli zapamiętamy sumy prefiksowe

f(i,j) - największa wartość bezwzględna wyniku tymczasowego przy dodawaniu liczb od ni do nj
f(i,i+1) = abs(ni + nj)
dla j > i+1
f(i,j) = max{ abs(sum(i,j)), min{f(i,j-1),f(i+1,j)}}

'''
