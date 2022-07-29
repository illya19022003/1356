import math

print("Завдання 1")
s = [int(input(": ")), int(input(": ")), int(input(": "))]  # task1
b = list(filter(lambda x: x >= 1 and x <= 3, s))
print(b)

print("Завдання 2")
year = int(input("Введiть рiк: "))  # task2
if year % 400 == 0 or year % 4 == 0 and not year % 100 == 0:
    print("366 днiв")
else:
    print("365 днiв")

print("Завдання 3")
price = int(input("Введiть суму: "))  # task3
if price >= 0 and price < 500:
    print("До сплати:", price)
elif price >= 500 and price < 1000:
    print("До сплати:", price - price * 3 / 100)
elif price >= 1000:
    print("До сплати:", price - price * 5 / 100)

print("Завдання 4")
ld = [4, 6, 2, 12]  # task4
print(math.cos(min(ld)))

print("Завдання 5")
l2 = [2, 4, 6]  # task5
print(math.sin(max(l2)))

print("Завдання 6")
a = int(input("Введiть а: "))  # task6
b = int(input("Введiть b: "))
s = (b / 2) * math.sqrt((a + b / 2) * (a - b / 2))
if s % 2 == 0:
    print(s / 2)
else:
    print("Не можу подiлити на 2")

print("Завдання 7")
mounth = ["january", "fabruary", "march", "april", "may",  # task7
          "june", "july", "august", "september", "october",
          "november", "december"]
num = int(input("Введiть номер мiсяця: "))
print(mounth[num-1])

print("Завдання 8")
numbers = [2, -4, 6]  # task8
fnums = list(filter(lambda x: x >= 0, numbers))
print(len(fnums))

print("Завдання 9")
a = int(input("Введiть а: "))  # task9
b = int(input("Введiть b: "))
s = 0
for i in range(a, b+1):
    s += i
print(s)

print("Завдання 10")
a = int(input("Введiть а: "))  # task10
b = int(input("Введiть b: "))
s = 0
for i in range(a, b+1):
    s += i**2
print(s)

print("Завдання 11")
a = int(input("а = "))  # task11
s = 0
j = 0
for i in range(a, 201):
    s += i
    j += 1
print(s/j)

print("Завдання 12")
a = int(input("Введiть а: "))  # task12
b = int(input("Введiть b: "))
s = 0
while a <= b:
    s += a
    a += 1
print(s)

print("Завдання 13")
a = int(input("Введiть а: "))  # task13
s = 0
for i in range(a, 50):
    s += i**2
print(s)

print("Завдання 14")
n = int(input("Введiть n: "))  # task14
k = 0
while 5**k <= n:
    k += 1
print(k)

print("Завдання 15")
n = int(input("Введiть n: "))  # task15
for i in range(100000):
    if i > n:
        print(i)
        break

print("Завдання 16")
n = int(input("Введiть n: "))  # task16
i = 0
while n >= i:
    i += 1
print(i)
