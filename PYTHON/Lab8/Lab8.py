import random
import time


class Bank:     # task 1
    def __init__(self, balance=0):
        self.__balance = balance

    def put_money(self, x=0):
        if x >= 0:
            self.__balance += x

    def withdraw_money(self, x=0):
        if self.__balance >= x and x >= 0:
            self.__balance -= x
        else:
            print('Недостатньо коштiв!')

    def check_balance(self):
        return self.__balance


print('\nЗавдання 1')
myBalance = Bank(360)
myBalance.put_money(5860)
myBalance.withdraw_money(4000)
print('Баланс: ', myBalance.check_balance())


class Coin:     # task 2
    def __init__(self, sideup):
        if sideup == 'haeds' or sideup == 'tails':
            self.__sideup = sideup
        else:
            self.__sideup = 'heads'

    def toss(self):
        if random.random() > 0.5:
            print('Орел!')
            self.sideup = 'heads'
        else:
            print('Решка')
            self.sideup = 'tails'


print('\nЗавдання 2')
coin = Coin('tails')

while True:
    try:
        n = int(input('Введiть к-ть пiдкидань: '))
        break
    except Exception as e:
        print('Введiть цiле число!', e)
for i in range(n):
    coin.toss()

print('Сторона:', coin.sideup)


class Car:      # task 3
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5
        if self.speed < 0:
            self.speed = 0

    def get_speed(self):
        return self.speed


print('\nЗавдання 3')
toyota = Car('Toyota', 'RAV4', 2022, 80)
for i in range(5):
    toyota.accelerate()
    print(f'Швидкiсть {toyota.get_speed()} km/h')
print()
for i in range(5):
    toyota.brake()
    print(f'Швидкiсть {toyota.get_speed()} km/h')


class Pets:     # Task 4
    pets_list = []


class Dog(Pets):
    mammal = True
    breed: str
    nature: str

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Pets.pets_list.append(self)

    def __str__(self):
        return f'Кличка: {self.name}. Вiк: {self.age}'


class Labr(Dog):
    breed = 'Labr'
    nature = 'Добрий'

    def behavior(self):
        return f'Характер: {Labr.nature}'


class Doberman(Dog):
    breed = 'Labr'
    nature = 'Злий'

    def behavior(self):
        return f'Характер: {Doberman.nature}'


print('Завдання 4')
tom = Labr('Tom', 2)
rex = Doberman('Rex', 5)

for i in Pets.pets_list:
    print(i)


class Buffer:       # task 5
    def __init__(self):
        self.__buffer = []

    def add(self, a):
        for i in a:
            self.__buffer.append(i)
        while len(self.__buffer) >= 5:
            print(f'Сума п\'яти елементiв: {sum(self.__buffer[0:5])}')
            del self.__buffer[0:5]

    def get_current_part(self):
        return self.__buffer


arr = [i for i in range(1, 51)]
buff = Buffer()
i = 0
while i < len(arr):
    x = random.randint(1, 10) + i
    print(buff.get_current_part())
    buff.add(arr[i:x])
    i = x
    time.sleep(0.1)


class MyException(Exception):       # task 6
    def __init__(self, text):
        if len(text) < 10:
            raise ValueError('Помилка, ім\'я менше 10 символів')


name = input('Введiть iмя: ')
MyException(name)


class RomanDec:     # task 7
    """Клас RomanDec"""

    @staticmethod
    def converte_to_rome(dec):
        """Приймає десяткове число і повертає число у
        римській системі числення"""
        numbers = zip([1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
                      ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X",
                      "IX", "V", "IV", "I"])
        result = []
        for d, r in numbers:
            while dec >= d:
                result.append(r)
                dec -= d
        return ''.join(result)

    @staticmethod
    def converte_to_dec(rome):
        """Приймає число у римській системі числення
        і повертає десяткове число"""
        res = 0
        numbers = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for i in range(len(rome)-1):
            if (numbers[rome[i]] < numbers[rome[i+1]]):
                res = res - numbers[rome[i]]
            elif (numbers[rome[i]] >= numbers[rome[i+1]]):
                res = res + numbers[rome[i]]

        res = res + numbers[rome[len(rome)-1]]

        return res


print(RomanDec().converte_to_rome(464))
print(RomanDec().converte_to_dec('IV'))


class Shop:     # task 8
    def __init__(self, shop_name, store_type, number_of_units=0):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units

    def describe_shop(self):
        print(f'Назва: {self.shop_name}. Тип: {self.store_type}')

    def open_shop(self):
        print('Магазин вiдкрито!')

    def set_number_of_units(self, num):
        self.number_of_units = num

    def increment_number_of_units(self, num):
        if num > 0:
            self.number_of_units += num


# a)
print('Завдання 8')
print('\na)')
store = Shop('Кроп', 'Магазин одягу')
print(f'-{store.store_type}\n-{store.shop_name}')
store.describe_shop()
store.open_shop()

# b)
print('\nb)')
store1 = Shop('Ашан', 'Супермаркет')
store2 = Shop('Фокстрот', 'Магазин техники')
store3 = Shop('МузТорг', 'Магазин муз. iнструментiв')

store1.describe_shop()
store2.describe_shop()
store3.describe_shop()

# c)
print('\nc)')
store = Shop('Кроп', 'Магазин одягу', 15)
print(f'К-ть товару: {store.number_of_units}')
store.number_of_units = 10
print(f'К-ть товару: {store.number_of_units}')

# d)
print('\nd)')
store.set_number_of_units(20)
print(f'К-ть товарiв: {store.number_of_units}')
store.increment_number_of_units(8)
print(f'Нова к-ть товарiв: {store.number_of_units}')


class Discount(Shop):   # e)
    def __init__(self, arr):
        self.disk_arr = arr

    def get_discounts_ptoducts(self):
        print(self.disk_arr)


print('\ne)')
store_discount = Discount(['Барнi', 'Пепсi', 'Чернiгiвське',
                           'Пiцца', 'Хлiб'])
store_discount.get_discounts_ptoducts()


class User:  # task 9
    def __init__(self, first_name, last_name, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f'Iмя: {self.first_name}, Прiзвище: {self.last_name}')

    def greeting_user(self):
        print(f'Вiтаю вас, {self.first_name} {self.last_name}!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# a)
print('\na)')
print('Завдання 9')
vlad = User('Влад', 'Шпiнь')
misha = User('Миша', 'Зелiнський')

vlad.describe_user()
vlad.greeting_user()
misha.describe_user()
misha.greeting_user()

# b)
print('\nb)')
for i in range(15):
    vlad.increment_login_attempts()
print(vlad.login_attempts)

vlad.reset_login_attempts()
print(vlad.login_attempts)

# c)


class Admin(User):
    def __init__(self, first_name, last_name, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.privileges = ['Allowed to add message', 'Allowed to delete users',
                           'Allowed to ban users']
        self.login_attempts = login_attempts

    def show_privileges(self):
        print(self.privileges)


print('\nc)')
admin = Admin('Админ', 'Админыч')
admin.show_privileges()
