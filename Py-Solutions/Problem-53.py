import math

print(sum([1 for n in range(101) for r in range(n + 1) if math.factorial(n)/(math.factorial(r)*math.factorial(n-r)) > 1000000]))