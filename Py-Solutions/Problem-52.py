i = 1
answer = 0
while answer == 0:
  if set(str(i*1)) == set(str(i*2)):
    if set(str(i*2)) == set(str(i*3)):
      if set(str(i*3)) == set(str(i*4)):
        if set(str(i*4)) == set(str(i*5)):
          if set(str(i*5)) == set(str(i*6)):
            answer = i
  i += 1

print(answer)