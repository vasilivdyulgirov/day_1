# Второ решение — по-малко променливи

x = int(input("x = "))

a = x // 100
b = (x // 10) % 10
c = x % 10

print("sum =", a + b + c)
print("pr =", a * b * c)
