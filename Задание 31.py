X, Y = map (int, input('Введите X и Y через пробел: ').split())
A = (X % Y) * (Y % X)
B = int(not A)
print(B)
