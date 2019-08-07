class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.count = 0
        self.capacity = capacity

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        print (f"count={self.count} capacity={self.capacity}")
        if v > (self.capacity-self.count):
            print('False')
            return False
        else:
            print('True')
            return True

    def add(self, v):
        # положить v монет в копилку
        if self.can_add(v):
            self.count += v
            print (self.count,'  ',self.capacity)

x = MoneyBox(15)
x.add(5)
x.add(9)
x.add(1)
x.add(3)

