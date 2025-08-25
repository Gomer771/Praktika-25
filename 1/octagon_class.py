#импортируем библиотеки
import math
import matplotlib.pyplot as plt

class Octagon:

    #добавляем атрибуты
    def __init__(self, side_length):
        self.side_length = side_length
        self.angle = 135
        self.k = 1 + math.sqrt(2)

    #площадь описанной окружности
    def circumscribed_circle_square(self):
        return math.pi * self.circumscribed_circle_radius() ** 2

    #радиус вписанной окружности
    def inscribed_circle_radius(self):
        return self.side_length * self.k / 2

    #радиус описанной окружности
    def circumscribed_circle_radius(self):
        return self.side_length / (math.sqrt(2 - math.sqrt(2)))

    
    #площадь октагона
    def octagon_square(self):
        return 2 * self.side_length ** 2 * self.k
    
    #площадь вписанной окружности
    def inscribed_circle_square(self):
        return math.pi * self.inscribed_circle_radius() ** 2

    #периметр октагона
    def octagon_perimeter(self):
        return 8 * self.side_length

    #внутренний угол октагона
    def internal_angle(self):
        return (8 - 2) * 180 / 8  # 135 градусов

    #отрисовка графика
    def draw_figures(self):
        fig, ax = plt.subplots()  # создаем фигуру и оси для графика

        angles = [n * (360 / 8) for n in range(8)]  # вычисляем углы для 8 вершин октагона
        x = [self.circumscribed_circle_radius() * math.cos(math.radians(angle)) for angle in angles]  # координаты x
        y = [self.circumscribed_circle_radius() * math.sin(math.radians(angle)) for angle in angles]  # координаты y
        ax.plot(x + [x[0]], y + [y[0]], 'b-', label='Октагон')  # рисуем октагон

        # описанная окружность
        circle = plt.Circle((0, 0), self.circumscribed_circle_radius(), color='r', fill=False, label='Описанная окружность')
        ax.add_artist(circle)

        # вписанная окружность
        circle_inscribed = plt.Circle((0, 0), self.inscribed_circle_radius(), color='g', fill=False, label='Вписанная окружность')
        ax.add_artist(circle_inscribed)

        ax.set_aspect('equal')  # равные оси
        plt.legend()
        plt.show()