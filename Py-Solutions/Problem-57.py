# In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

sequence = [1,3]
for _ in range(1000):
  sequence.append(2*sequence[-1] + sequence[-2])

denominators = [2]
for i in range(1000):
  denominators.append(3*denominators[i] - sequence[i])

numerators = sequence[1:]

count = 0
for i in range(1000):
  if len(str(numerators[i])) > len(str(denominators[i])):
    count += 1

print(count)