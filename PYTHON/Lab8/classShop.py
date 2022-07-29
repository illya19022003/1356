class Shop:
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
