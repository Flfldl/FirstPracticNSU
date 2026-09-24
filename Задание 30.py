ATT = int(input('Введите ATT: '))
COMP = int(input('Введите COMP: '))
YDS =  int(input('Введите YDS: '))
TD = int(input('Введите TD: '))
INT = int(input('Введите INT: '))
a = (COMP / ATT - 0.3) * 5
b = (YDS / ATT - 3) * 0.25
c = (TD / ATT) * 20
d = 2.375 - (INT / ATT * 25)
e = (a + b + c + d) / 6
f = e * 100
print(f)