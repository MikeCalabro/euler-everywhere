# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

total_list = []
for a in range(1,2000):
  for b in range(a,2000):
    string = []
    string.append(str(a))
    string.append(str(b))
    string.append(str(a*b))
    final = "".join(string)
    if len(final) == 9:
      if len(final) == len(set(final)):
        if '0' not in set(final):
          total_list.append(a*b)

print(sum(set(total_list)))
