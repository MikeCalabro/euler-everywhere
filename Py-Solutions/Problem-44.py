# Find the pair of pentagonal numbers for which their sum and difference are pentagonal and D is minimised; what is the value of D?

pents = set(n*(3*n-1)/2 for n in range(1,10000))

def pentSum(a,b):
  return a + b in pents

def pentDif(a,b):
  return a - b in pents

for i in pents:
  for j in pents:
    if pentSum(i,j) and pentDif(i,j):
      print(i,j,i-j)
