from datetime import datetime, timedelta
from typing import List
import csv


# task 1
print('Завдання 1:')
fstFile = open('numbers.txt', 'r')
lis = list(fstFile.read().split('\n'))
fstFile.close()
lis = [int(i) for i in lis]
print(sum(lis))
scndFile = open('sum_numbers.txt', 'w')
scndFile.write(f'{sum(lis)}')
scndFile.close()

# Task 2
print('Завдання 2:')
x = 1
task2file = open('lab6Task2.txt', 'w', encoding='utf8')
while x != 0:
    try:
        x = int(input('Введіть число x (натисніть 0 щоб вийти): '))
        if x != 0:
            task2file.write(f'{x} - парнiсть: {x%2==0}\n')
        print("готово")
    except Exception as e:
        print('Введiть цiле число!', e)
task2file.close()

# Task 3
print('Завдання 3:')
textList = []
file = open('learning_python.txt', 'r', encoding='utf8')
for i in file:
    textList.append(i.replace('\n', ''))
file.close()
textList.sort(key = len)
textList.reverse()
print(textList)

# Task 4
print('Завдання 4:')
import os
try:
    import shutil
    shutil.rmtree('task4')
except:
    print('Створено task4')
os.mkdir('task4')

textList2 = []
for i in textList:
    textList2.append(i.replace('Python', 'C#'))

for i in textList2:
    flag = 0
    while flag < 1 or flag > 2:
        try:
            print(i, '\nЯкщо твердження вiрне натиснiть 1\nЯкщо твердження вiрне натиснiть 2')
            flag = int(input('Вiдповiдь: '))
        except:
            print('     Введіть ціле число!!!')
    if flag == 1:
        trueFile = open('task4/true.txt', 'a', encoding='utf8')
        trueFile.write(f'{i}\n')
        trueFile.close()
    if flag == 2:
        falseFile = open('task4/false.txt', 'a', encoding='utf8')
        falseFile.write(f'{i}\n')
        falseFile.close()

# task 5
print('Завдання 5:')
import datetime

if os.path.exists('guest_book.txt') == False:
    guestFile = open('guest_book.txt', 'w', encoding='utf8')
    guestFile.write('Час створення файлу: ' + str(datetime.datetime.now()) + '\n')
    guestFile.close()
name = 'name'
guestFile = open('guest_book.txt', 'a', encoding='utf8')
while True:
    name = input('Введіть і\'мя (натиснiть 0 щоб вийти): ')
    if name == '0':
        break
    greeting = f'Вітаю вас, {name}!'
    print(greeting)
    guestFile.write(greeting + ' ' + str(datetime.datetime.now()) + '\n')
guestFile.close()

# Task 6
print('Завдання 6:')
aboutPython = open('about_python.txt', 'r')
pyText = ''
for i in aboutPython:
    pyText += i
aboutPython.close()
check = input('Введіть слово або символ для знаходження його в тексті: ')

start = datetime.datetime.now()
start = start.minute*60 + start.second

count = pyText.lower().count(check.lower())
print(f'Кількість "{check}" у тексті: {count}')

finish = datetime.datetime.now()
finish = finish.minute*60 + finish.second

time = finish - start
if os.path.exists('about_python_stats.txt') == False:
    guestFile = open('about_python_stats.txt', 'w', encoding='utf8')
    guestFile.write('Час створення файлу: ' + str(datetime.datetime.now()) + '\n')
    guestFile.close()

stats = open('about_python_stats.txt', 'a', encoding='utf8')
stats.write(f'Кількість "{check}" у тексті: {count}. Час перевірки: {datetime.datetime.now()}. Виконано за {finish - start} секунд\n')

# Task 7
def count():
    count = 0
    with open('marks.lab6.csv') as f:
        f_reader = csv.reader(f, delimiter=',')
        for row in f_reader:
            count += 1
    return count


def marks():
    with open('marks.lab6.csv') as f:
        f_reader = csv.reader(f, delimiter=',')
        for row in f_reader:
            print(f"Студент {row[0]} набрав {row[4]} балів")


def time_mark(time):
    with open('marks.lab6.csv') as f:
        f_reader = csv.reader(f, delimiter=',')
        for row in f_reader:
            _sum = 0
            for i in range(1, time + 1):
                try:
                    _sum += float(row[i + 4].replace(',', '.'))
                except ValueError:
                    _sum += 0
            print(f"Студент {row[0]} отримав {_sum} за {time} хвилин")


def correct_wrong(k, count):
    correct = 0
    wrong = 0
    with open('marks.lab6.csv') as f:
        f_reader = csv.reader(f, delimiter=',')
        for row in f_reader:
            if row[k] == '0,50':
                correct += 1
            else:
                wrong += 1
    return f"має {round((correct * 100) / count, 0)}% правильних і {round((wrong * 100) / count, 0)}% неправильних"


def best_marks(k):
    lst_time = []
    lst_marks = []
    ratio = []
    students = []

    with open('marks.lab6.csv', encoding='utf-8') as f:
        f_reader = csv.reader(f, delimiter=',')
        for row in f_reader:
            try:
                _time = time.strptime(row[3], '%M хв %S сек')
            except ValueError:
                _time = time.strptime(row[3], '%M хв')
            lst_time.append(timedelta(hours=_time.tm_hour, minutes=_time.tm_min, seconds=_time.tm_sec).seconds)
            lst_marks.append(float(row[4].replace(',', '.')))
            students.append(row[0])

    for i in range(len(lst_marks)):
        ratio.append(lst_marks[i] / lst_time[i])
    ratio = array(ratio)
    ind = argpartition(ratio, -5)[-5:]
    return f"Найкраща оцінка {lst_marks[ind[k]]} з часом виконання {timedelta(seconds=lst_time[ind[k]])} у студента {students[ind[k]]}\n "

print("\nЗавдання 7")
count = count()  # 1
print(f"Кількість студентів: {count}")
print("--------------------------------------------------------------")
marks()  # 2
print("--------------------------------------------------------------")
time_kmr = int(input("\nВведіть час: "))  # 3
time_mark(time_kmr)
print("--------------------------------------------------------------")

with open('result.txt', 'w', encoding='utf8') as f:
    k = 5
    for j in range(1, 21):  # 4
        f.write("Завдання %d %s\n" % (j, correct_wrong(k, count)))
        k += 1
    f.write("\n")
    for i in range(5):  # 5
        f.write(best_marks(i))
