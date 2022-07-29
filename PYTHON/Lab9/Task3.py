class Apple:
    states = ['Вiдсутне', 'Цвiтiння', 'Зелене', 'Червоне']

    def __init__(self, index):
        self._index = index
        self.state = 0
        self._state = Apple.states[self.state]

    def grow(self):
        if self.state < 3:
            self.state += 1
            self._state = Apple.states[self.state]

    def is_ripe(self):
        if self.state == 3:
            return True
        return False


class AppleTree:
    def __init__(self, num=1):
        self.apples = []
        for i in range(num):
            apple = Apple(i)
            self.apples.append(apple)

    def grow_all(self):
        for i in self.apples:
            i.grow()

    def all_are_ripe(self):
        for i in self.apples:
            if i.is_ripe() == False:
                return False
        return True

    def give_away_all(self):
        if self.all_are_ripe() == True:
            self.apples.clear()


class Gardener:
    def __init__(self, name, tree):
        self.name = name
        self._tree = tree

    def work(self):
        self._tree.grow_all()

    def harvest(self):
        if self._tree.all_are_ripe() == True:
            self._tree.give_away_all()
        else:
            print('Ще не всi яблука дозрiли!')


def apple_base(tree):
    print(f'Список яблок({len(tree.apples)}):')
    for i in tree.apples:
        print(i._state)


tree = AppleTree(5)
worker = Gardener('Влад', tree)
apple_base(tree)

worker.work()
worker.harvest()
worker.work()
worker.work()
worker.harvest()
apple_base(tree)
