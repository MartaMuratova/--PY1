import doctest


class Pot:
    def __init__(self, capacity_volume: float, number_of_potatoes: int):
        """
        Создание и подготовка к работе объкта "Кастрюля"
        :param capacity_volume: Объем кастрюли
        :param number_of_potatoes: Количество картошки, помещаемой в кастрюлю
        Примеры:
        >>> pot = Pot(500,0) #инициализация экземпляра класса
        """

        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем кастрюли должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем кастрюли должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(number_of_potatoes, int):
            raise TypeError("Количество картофеля должно быть int")
        if number_of_potatoes < 0:
            raise ValueError("Количество картофеля не может быть отрицательным числом")
        self.number_of_potatoes = number_of_potatoes

    def does_Pot_has_one_potato_inside (self) -> bool:
        """
        Функция которая проверяет есть ли в кастрюле минимум одна картошка уже
        :return: Пустая ли кастрюля
        Примеры:
        >>> pot = Pot(500, 1)
        >>> pot.does_Pot_has_one_potato_inside()
        """
        ...

    def put_potatoes_in_Pot(self, number_of_potatoes: int) -> None:
        """
        Положить картошку в кастрюлю.
        :param number_of_potatoes: Количество картофеля
        :raise ValueError: Если количество добавляемого картофеля превышает объем кастрюли, то вызываем ошибку
        Примеры:
        >>> pot = Pot(500,0)
        >>> pot.put_potatoes_in_Pot(40)
        """
        if not isinstance(number_of_potatoes, int):
            raise TypeError("Количество картофеля должено быть типа int")
        if number_of_potatoes< 0:
            raise ValueError("Число добавляемого картофеля должено быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass