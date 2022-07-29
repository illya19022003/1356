import datetime

# task 1
class Person:
    def __init__(self, surname, first_name,  birth_date, nickname=''):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname
        try:
            birth_date = birth_date.split('-')
        except Exception as e:
            print(e)
        try:
            self.birth_date = datetime.date(int(birth_date[0]), int(birth_date[1]), int(birth_date[2]))
        except Exception as e:
            print('Неправильний формат дати!', e)
            self.birth_date = 'Помилка'

    def __str__(self):
        return f'Iмя: {self.surname} {self.first_name}. Псевдонiм: {self.nickname}. Дата народження: {self.birth_date}'

    def get_fullname(self):
        return f'{self.surname} {self.first_name}'

    def get_age(self):
        try:
            return datetime.date.today().year - self.birth_date.year
        except Exception as e:
            return 'Помилка ' + e


vlad = Person('Шпiнь', 'Владислав', '2002-10-31')
print(f'Iмя: {vlad.get_fullname()}\nВiк: {vlad.get_age()}\n')

# task 2
persons = open('persons.txt', 'r', encoding='utf8')
person_list = persons.read().split('\n')
persons.close()
object_list = []
for i in person_list:
    object_list.append(Person(i.split(' ')[0], i.split(' ')[1], i.split(' ')[2]))

persons = open('persons.txt', 'w', encoding='utf8')
for i in range(len(object_list)):
    persons.write(person_list[i] + '\n')
    persons.write(f'Iмя: {object_list[i].get_fullname()}\nВiк: {object_list[i].get_age()}\n')
persons.close()
