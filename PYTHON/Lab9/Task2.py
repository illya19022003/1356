class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price - (self._price / 100 * discount)


class SmallHouse(House):
    def __init__(self, price, area=40):
        self._price = price
        self._area = area


class Human:
    default_age = 19
    default_name = 'Влад'

    def __init__(self, name=default_name, age=default_age, money=1000, house=False):
        self.money = money
        self.house = house
        self.name = name
        self.age = age

    def info(self):
        print(f'Iмя: {self.name}\nВiк: {self.age}\nДiм: {self.house}\nБаланс: {self.money}грн')

    def default_info():
        print(f'Стандартне iмя: {Human.default_name} - {Human.default_age} рокiв')

    def __make_deal(self, house, discount):
        self.house = house
        self.money -= house.final_price(discount)

    def buy_house(self, house, discount=10):
        if house.final_price(discount) <= self.money:
            self.__make_deal(house, discount)
        else:
            print('-Недостатньо коштiв!')

    def earn_money(self, money):
        self.money += money


Human.default_info()

person1 = Human('Алина', 27, 2000)
person1.info()

small = SmallHouse(5000)
person1.buy_house(small)
person1.earn_money(5000)
person1.buy_house(small)
person1.info()
