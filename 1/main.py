# импорт класса
from octagon_class import Octagon

def main():
    # создаем объект Octagon(длинна стороны 5)
    octagon = Octagon(5)

    print(f"Радиус описанной окружности: {octagon.circumscribed_circle_radius()}")
    print(f"Площадь описанной окружности: {octagon.circumscribed_circle_square()}")
    print(f"Радиус вписанной окружности: {octagon.inscribed_circle_radius()}")
    print(f"Площадь вписанной окружности: {octagon.inscribed_circle_square()}")
    print(f"Площадь октагона: {octagon.octagon_square()}")
    print(f"Периметр октагона: {octagon.octagon_perimeter()}")
    print(f"Внутренний угол октагона: {octagon.internal_angle():}°")

    octagon.draw_figures()

if __name__ == '__main__':
    main()
