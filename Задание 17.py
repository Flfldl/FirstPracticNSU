A = int(input("Введите рост в дюймах: "))
B = int(input("Введите вес в фунтах: "))
C = (B * 703) / A**2
D = round(C, 2)
print(D)