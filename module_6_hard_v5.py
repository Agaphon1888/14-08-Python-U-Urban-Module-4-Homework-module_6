# Дополнительное практическое задание по модулю: "Наследование классов."
# Задание "Они все так похожи".


from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = list(color)
        self.filled = True

        if not self.__is_valid_sides(*sides):
            # Если переданное количество сторон некорректно, заполним единицами
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return (
                all(isinstance(side, int) and side > 0 for side in new_sides)
                and len(new_sides) == self.sides_count
        )

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color, circumference)
        self.__radius = self.get_radius()

    def get_radius(self):
        return self.get_sides()[0] / (2 * pi)

    def get_square(self):
        radius = self.get_radius()
        return pi * (radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, a, b, c):
        super().__init__(color, a, b, c)

    def get_square(self):
        a, b, c = self.get_sides()
        hp = (a + b + c) / 2  # hp = half-perimeter = полупериметр
        return sqrt(hp * (hp - a) * (hp - b) * (hp - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, edge_length):
        super().__init__(color)
        self.__sides = [edge_length] * self.sides_count

    def get_volume(self):
        return self.__sides[0] ** 3

    def get_sides(self):
        return self.__sides  # Возвращает рёбра куба


def main():
    # Примеры использования
    circle1 = Circle((200, 200, 100), 10)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())  # [55, 66, 77]
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())  # [222, 35, 130]

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())  # [15]

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))  # 15

    # Проверка объёма (куба):
    print(cube1.get_volume())  # 216


if __name__ == '__main__':
    main()
