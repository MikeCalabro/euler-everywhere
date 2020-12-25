# There are exactly four non-trivial examples of this type of fraction, 
# less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

product = 1

for a in range(10,100):
  for b in range(10,100):
    if str(b)[1] != "0":
      if str(a)[0] != str(a)[1]:
        if str(b)[0] != str(b)[1]:
          if float(a)/b == float(str(a)[0]) / int(str(b)[1]):
            if str(a)[1] == str(b)[0]:
              product *= float(a)/float(b)

print(product)
print(float(1)/100)
print(100)