text = input("Текст: ")  # task 1
letter = input("Буква: ")
text2 = text.split()

print(f"Слова на букву {letter}: ")

for i in text2:
    if i.lower().find(letter) == 0:
        print(i)

text = text.replace(':', "%")  # tast 2

x = 0  # task 3
for i in text:
    if i == '.':
        text = text.replace(i, "")
        x += 1
print("К-ть видалених крапок:", x)

x = 0  # task 4
for i in text:
    if i == 'а':
        x += 1
text = text.replace('а', "о")
print("\n", text)
print("\nК-ть замiн 'а' на 'о':", x)

text = text.lower()  # task 5
text2 = text.split()

x = 0  # task 6
for i in text:
    if i == 'о':
        x += 1
print("К-ть видалених о:", x)
text = text.replace('о', "")

text3 = text[:len(text)//2]  # task 7
text = text[len(text)//2:]
text = text3.replace('п', "*") + text

word = input("\nСлово: ")  # task 8
x = 0
for i in text2:
    if i == word:
        x += 1
print(f"Слово {word} зустрiчаеться {x} раз")
print("\n", text)

text = input("\nТекст на английском: ")  # task 9
text3 = text.split()
text2 = text.split()
x = 0
for i in text2:
    text2[x] = i[0].upper()+i[1:]
    x += 1
text = ' '.join(text2)
print("\n\n", text)

n = input("n = ")  # task 10
p = input("p = ")
print(f"Слова на букву {n}: ")

for i in text2:
    if i.lower().find(n) == 0:
        print(i)
print(f"Слова закiнчуються на букву {p}: ")

for i in text2:
    if p == i[-1]:
        print(i)

letters = "a e i o u y h"  # task 11
x = 0
for i in text.lower():
    if letters.find(i) >= 0 and i != ' ':
        x += 1
print("Голосних лiтер:", x)

letters2 = "b c d f g j k l m n p r s t v w x z"  # task 12
x = 0
for i in text.lower():
    if letters2.find(i) >= 0 and i != ' ':
        x += 1
print("Приголосних лiтер:", x)

i = 0
while i < len(text3):
    if text3[i] == text3[i].lower():
        del text3[i]
        i -= 1
    i += 1
print(text3)
