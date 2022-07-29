a = float(input("a: "))  # Завдання 1
b = float(input("b: "))
c = int(input("c: "))
d = int(input("d: "))

s = [a+b, a-c, a*d, d/b, b**c, d//c, c % a]  # Завдання 2
print(s)

print("Довжина списка:", len(s))  # Завдання 3
for i in s:
    if i % 2 == 0:
        print(i)

s[2], s[5] = s[5], s[2]  # Завдання 4
print(s)

name = input("Введiть iмя: ")  # Завдання 5
print(f"\nЛабораторна робота №1\nВиконав: {name}\nВисновок: я ознайомився з мовою Python")
