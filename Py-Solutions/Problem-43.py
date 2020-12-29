from itertools import permutations  

my_list = list(permutations("0123456789"))

total = 0
for i in my_list:
  if i[0] != 0 and int("".join(i[1:4])) % 2 == 0 and int("".join(i[2:5])) % 3 == 0 and int("".join(i[3:6])) % 5 == 0 and int("".join(i[4:7])) % 7 == 0 and int("".join(i[5:8])) % 11 == 0 and int("".join(i[6:9])) % 13 == 0 and int("".join(i[7:])) % 17 == 0:
    print("".join(i))
    total += int("".join(i))

print(total)
