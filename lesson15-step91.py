class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.buffer = []
        # print (self.buffer)

    def add(self, *a):
        # добавить следующую часть последовательности
        self.buffer.extend(a)
        # print (self.buffer,' ',len(a), len(self.buffer),)
        while len(self.buffer) >= 5:
            summ = 0
            for i in range(5):
                summ += self.buffer.pop(0)
            print(summ)
            
    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были     
        # добавлены
        if self.buffer == []: print('empty')
        print(self.buffer)
        return self.buffer

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
print('-----')
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]