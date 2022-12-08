import doctest


class Bulb:
    def __init__(self, base_diameter: float, color_temperature: int, diameter_of_the_hole: float):
        """
        Создание и подготовка к работе объкта "Лампочка"
        :param base_diameter: Диаметр цоколя лампочки
        :param color_temperature: Цветовая температура
        :param diameter_of_the_hole: Диаметр отверстия в люстре
        Примеры:
        >>> buld = Bulb(27,2700, 27) #инициализация экземпляра класса
        """

        if not isinstance(base_diameter, (int, float)):
            raise TypeError("Диаметр цоколя должен быть типа int или float")
        if base_diameter <= 0:
            raise ValueError("Диаметр цоколя должен быть положительным числом")
        self.base_diameter = base_diameter

        if not isinstance(color_temperature, int):
            raise TypeError("Цветовая тампература должна быть int")
        if color_temperature < 0:
            raise ValueError("Цветовая тампература не может быть отрицательным числом")
        self.color_temperature = color_temperature

        if not isinstance(diameter_of_the_hole, (int, float)):
            raise TypeError("Диаметр отверстия лампы должен быть типа int или float")
        if diameter_of_the_hole <= 0:
            raise ValueError("Диаметр отверстия лампы должен быть положительным числом")
        self.diameter_of_the_hole = diameter_of_the_hole

    def screw_the_bulb_into(self) -> bool:
        """
        Функция которая проверяет совпадает ли диаметр цоколя с диаметром отверстия
        :return: Есть ли возможность вкрутить лампочку?
        Примеры:
        >>> buld = Bulb(27, 2700, 30)
        >>> buld.screw_the_bulb_into()
        """
        ...

    def check_if_the_light_is_on(self, color_temperature: int) -> None:
        """
        Проверить, горит ли лампочка
        :param color_temperature: Индикатор света
        :raise ValueError: Если значение индикатора = 0, то вызываем ошибку
        Примеры:
        >>> buld = Bulb(27, 0, 27)
        >>> buld.check_if_the_light_is_on(2700)
        """
        if not isinstance(color_temperature, int):
            raise TypeError("Цветовая тампература должна быть int")
        if color_temperature < 0:
            raise ValueError("Цветовая тампература не может быть отрицательным числом")
        self.color_temperature = color_temperature
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass