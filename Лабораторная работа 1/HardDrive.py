# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class HardDrive:
    def __init__(self, capacity_volume: float, occupied_volume: float, data_rate: float):
        """
        Создание и подготовка к работе объкта "Жесткий диск"
        :param capacity_volume: Объем памяти жесткого диска
        :param occupied_volume: Объем данных, необходимых в передаче на диск
        :param data_rate: Скорость передачи данных
        Примеры:
        >>> hard_drive = HardDrive(1000,0,0) #инициализация экземпляра класса
        """

        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем памяти должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем памяти должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Объем данных должен быть int или float")
        if occupied_volume < 0:
            raise ValueError("Объем передаваемых данных не может быть отрицательным числом")
        self.occupied_volume = occupied_volume
        self.data_rate = data_rate

    def does_HardDrive_has_enough_space (self) -> bool:
        """
        Функция которая проверяет достаточно ли места на диске для загрузки на него новой информации
        :return: Достаточно ли места на диске
        Примеры:
        >>> hard_drive = HardDrive(1000, 0, 120)
        >>> hard_drive.does_HardDrive_has_enough_space()
        """
        ...

    def add_data_on_HardDrive(self, data: float) -> None:
        """
        Загрузка данных на жесткий диск.
        :param data: Объем добавляемой информации
        :raise ValueError: Если количество добавляемой информации превышает свободное место на диске, то вызываем ошибку
        Примеры:
        >>> hard_drive = HardDrive(1000, 0,120)
        >>> hard_drive.add_data_on_HardDrive(1200)
        """
        if not isinstance(data, (int, float)):
            raise TypeError("Добавляемый объем информации должен быть типа int или float")
        if data < 0:
            raise ValueError("Добавляемый объем информации должен быть положительным числом")
        ...

    def speed_calculation(self, speed: float) -> None:
        """
        Вычисление скорости передачи данных.
        :param speed: Скорость передачи данных
        :raise ValueError: Если скорость передачи данных равна 0,то возвращается ошибка.
        :return: Реальная скорость передачи данных
        Примеры:
        >>> hard_drive = HardDrive(1000, 500, 150)
        >>> hard_drive.speed_calculation(0)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
