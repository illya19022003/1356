import random
s = list(map(int, input("List: ").split()))  # task 1
print(s)

s2 = list(filter(lambda x: x >= 0, s))  # task 2
s3 = list(filter(lambda x: x < 0, s))
print(s2, s3)

s = [i for i in range(1, 41, 2)]  # task 3
sum = 0
for i in range(len(s)):
    if i % 2 != 0:
        sum += s[i]
print(s, "\nCума непарних членiв:", sum)

s = []  # task 4
for i in range(30):
    s.append(random.randint(-100, 100))
s2 = s.copy()
s2.sort()
s2.reverse()
print(f"{s2}\nМаксимальний елемент: {max(s2)}, iндекс: {s.index(max(s2))}")

print("Парнi елементи з '-': ")  # task 5
for i in range(len(s)-1):
    if s[i] < 0 and s[i+1] < 0:
        print(s[i], s[i+1])

s = []  # task 6
s2 = []
for i in range(10):
    s.append(random.randint(-10, 10))
for i in s:
    if i < max(s):
        s2.append(i**2)
s2.sort()
s2.reverse()
print(max(s), s2)

for i in range(30):  # task 7
    s.append(random.randint(-100, 100))
    maxx = max(s)
for i in s:
    if abs(i) > max(s):
        maxx = i
print(s, "\nmax:", maxx)

s = []  # task 8
for i in range(30):
    s.append(random.randint(-100, 100))
ll = []
start = 0
fin = 3
for i in range(len(s)):
    ll.append(s[start:fin])
    start += 3
    fin += 3
    if start >= len(s):
        break
print(f"s = {s}\nll = {ll}")
