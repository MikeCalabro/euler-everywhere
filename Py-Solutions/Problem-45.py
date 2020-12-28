
limit = 100000

tris = set([n*(n+1)/2 for n in range(1,limit)])
pents = set([n*(3*n-1)/2 for n in range(1,limit)])
hexs = set([n*(2*n-1) for n in range(1,limit)])

print(tris.intersection(pents, hexs))
