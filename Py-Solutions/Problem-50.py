
def isPrime(num):
  if num < 2:
    return False
  elif num ==2:
    return True
  else:
    return sum([i for i in range(1, int(num**0.5) + 1) if num % i == 0]) == 1

prime_list = [i for i in range(10000) if isPrime(i)]

max_len = 0
for i in range(1000):
  sum_list = []
  while sum(sum_list) < 1000000:
    sum_list.append(prime_list[i])
    i += 1
  sum_list = sum_list[:-1]
  while not isPrime(sum(sum_list)):
    sum_list = sum_list[:-1]
  if len(sum_list) > max_len:
    max_len = len(sum_list)
    print(sum(sum_list), len(sum_list))














# I liked this approach, but it took way too long lol

# max_len = 0
# for i in prime_list:
#   sum_check = i
#   sum_arr = []
#   counter = 0
#   while sum(sum_arr) != sum_check:
#     if sum(sum_arr) < sum_check:
#       sum_arr.append(prime_list[counter])
#       counter += 1
#     if sum(sum_arr) > sum_check:
#       sum_arr = sum_arr[1:]
#   if len(sum_arr) > max_len:
#     max_len = len(sum_arr)
#     print(sum_arr, sum(sum_arr))
