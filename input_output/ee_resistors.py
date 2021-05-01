def par(x, y):
    return (x*y)/(x+y)


def d2s(i, j, k):
    return (i * j)/(i + j + k)


Rab = par(par(par(100+68, 560), 820) + 330, 220)
print('Rab = {} k'.format(Rab))

Rac = par(par(par(100+68, 560), 820) +220, 330)
print('Rac = {} k'.format(Rac))

Rbc = par(par(100+68, 560), par(220+330, 820))
print('Rbc = {} k'.format(Rbc))

Rbd = par(par(par(220+330, 820), 560) + 68, 100)
print('Rbd = {} k'.format(Rbd))

Rcd = par(par(par(220+330, 820), 560) + 100, 68)
print('Rcd = {} k'.format(Rcd))

r1 = par(560, 820)
Rad = par(220 + d2s(r1, 100, 68), 330 + d2s(r1, 68, 100)) + d2s(68, 100, r1)
print('Rad = {} k'.format(Rad))
