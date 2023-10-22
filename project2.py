x = int(input("Введіть число x: "))
y = int(input("Введіть число y: "))

x1 = {i for i in range(1, x + 1) if x % i == 0}
y1 = {i for i in range(1, y + 1) if y % i == 0}

c = x1.intersection(y1)

gcd = max(c)

print("Спільні дільники чисел x і y:", c)
print("Найбільший спільний дільник (НСД) чисел x і y:", gcd)
