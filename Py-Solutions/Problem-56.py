x = 695

answer = 0
for a in range(100):
  for b in range(100):
    check = sum([int(i) for i in str(a**b)])
    if check > answer:
      answer = check

print(answer)