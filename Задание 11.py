r = int(input('Введите первый радиус: '))
r1 = int(input('Введите второй радиус: '))
A = 3.14*(r)**2
B = 3.14*(r1)**2
if A > B:
    C = A - B
    print(C)
if A < B:
    D = B - A
    print(D)