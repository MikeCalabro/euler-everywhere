# For the first one hundred natural numbers, find the total of the digital sums
# of the first one hundred decimal digits for all the irrational square roots.
import decimal as d
from math import sqrt
d.getcontext().prec = 150

totalSum = sum([sum([int(j) for j in str(d.Decimal(i).sqrt())[2:101]]) + int(sqrt(i)) for i in [i for i in range(2,100) if sqrt(i) % 1 != 0]])

print(totalSum)
