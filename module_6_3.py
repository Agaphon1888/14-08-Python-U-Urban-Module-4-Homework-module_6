# Домашнее задание по теме "Множественное наследование".
# Задача "Мифическое наследование".

class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)  # вызываем метод из класса Horse
        self.fly(dy)  # вызываем метод из класса Eagle

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)  # выводим звук из атрибута экземпляра


def main():
    p1 = Pegasus()
    print(p1.get_pos())  # Начальная позиция (0,0)
    p1.move(10, 15)
    print(p1.get_pos())  # Позиция после первого движения (10, 15)
    p1.move(-5, 20)
    print(p1.get_pos())  # Позиция после второго движения (5, 35)
    p1.voice()  # Вывод звука Пегаса


if __name__ == '__main__':
    main()