class Jacket:
    """ Базовый класс куртки. """
    def __init__(self, color: str, size: int, sex='male'):
        self.color = color
        self.size = size
        self._sex = sex    #Защищенный атрибут
    """Куртка только  для мужчин"""

    def __str__(self):
        return f"Цвет куртки {self.color}. Размер куртки {self.size}. Пол {self._sex}"

    def __repr__(self):
        return f"{self.__class__.__name__}(color={self.color!r}, size={self.size!r}, _sex={self._sex!r})"

    def get_size(self, size: int):
        """ Присвоение размера куртки """
        if not isinstance(size, int):
            raise TypeError("Размер должен быть типа int")
        if size <= 0:
            raise ValueError("Значение должно быть положительным")

    def get_color(self, color: str):
        """ Присвоение цвета куртки """
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")


class Winter_jacket(Jacket):
    """ Дочерний класс куртки. Зимняя куртка """
    def __init__(self, color: str, size: int, sex='male', fluff=bool, big_size=int):
        super().__init__(color, size, sex)
        self.fluff = fluff   #"Добавим атрибут пух"
        self.big_size = big_size  #Дополнительный атрибут "большой размер"

    def fluff_in (self, fluff):
        """Функция уточнения добавления пуха в куртку"""
        fluff = 1
        if fluff != 1:
            print("Кажется в такой крутке Вы замерзнете")
        else:
            print("Куртка будет и правда теплой")

    def __repr__(self):
        return f"{self.__class__.__name__}(color={self.color!r}, size={self.size!r}, _sex={self._sex!r}, fluff={self.fluff!r}, big_size={self.big_size!r})"
    """Перегрузка была осуществлена с целью добавления атрибута, присущего только этому дочернему классу"""

    def get_size(self, big_size=int, size=int):
        super().get_size(size)
        if size > 10:
            size = big_size
    """ Данный метод был перегружен с целью дополнительной конфигурации размера"""


class Summer_jacket(Jacket):
    """ Дочерний класс куртки. Летняя куртка """
    def __init__(self, color: str, size: int, sex='male', hood="да"):
        super().__init__(color, size, sex)
        self.hood = hood
    """Добавим атрибут капюшон"""

    def hood_on (self, hood: str):
        """Функция уточнения добавления капюшона на куртку"""
        ans = "да"
        if hood is not ans:
            print("Куртка без капюшона")
        else:
            print("Куртка с капюшоном")

    def __repr__(self):
        return f"{self.__class__.__name__}(color={self.color!r}, size={self.size!r}, _sex={self._sex!r}, hood={self.hood!r})"
    """Перегрузка была осуществлена с целью добавления атрибута, присущего только этому дочернему классу"""


if __name__ == "__main__":
    rect = Jacket("pink", 10)
    print(rect.get_size(10))
    aff = Summer_jacket("да", 9)
    print(aff.hood_on("да"))
    win = Winter_jacket("black", 12)
    print(win.fluff_in(1))

    pass
