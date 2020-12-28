import math

def pythagoreanProduct(sum):
  final_sum = 0
  for a in range(1,int(round(sum/2))):
    for b in range(1,int(round(sum/2))):
      c = math.sqrt(a**2 + b**2)
      if c % 1 == 0 and a + b + int(c) == sum:
        final_sum += 1
  return final_sum/2

def main():
  print(max([[pythagoreanProduct(i),i] for i in range(10,1000)]))

if __name__ == '__main__':
  main()
  