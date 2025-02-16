class Car:
    """
    Базовый класс для автомобилей.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализация базового класса Car.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        """
        self._brand = brand  # Непубличный атрибут, чтобы защитить данные о марке
        self._model = model  # Непубличный атрибут, чтобы защитить данные о модели
        self.year = year

    def __str__(self) -> str:
        """
        Возвращает строковое представление автомобиля.

        :return: Строка с информацией об автомобиле.
        """
        return f"{self.year} {self._brand} {self._model}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление автомобиля.

        :return: Формальная строка с информацией об автомобиле.
        """
        return f"Car(brand='{self._brand}', model='{self._model}', year={self.year})"

    def start_engine(self) -> str:
        """
        Запускает двигатель автомобиля.

        :return: Сообщение о запуске двигателя.
        """
        return f"{self._brand} {self._model} engine started."


class Sedan(Car):
    """
    Класс для легковых автомобилей, наследующий от Car.
    """

    def __init__(self, brand: str, model: str, year: int, trunk_size: int) -> None:
        """
        Инициализация легкового автомобиля.

        :param brand: Марка легкового автомобиля.
        :param model: Модель легкового автомобиля.
        :param year: Год выпуска легкового автомобиля.
        :param trunk_size: Объем багажника в литрах.
        """
        super().__init__(brand, model, year)  # Вызов конструктора базового класса
        self.trunk_size = trunk_size  # Объем багажника

    def __str__(self) -> str:
        """
        Возвращает строковое представление легкового автомобиля.

        :return: Строка с информацией о легковом автомобиле.
        """
        return f"{super().__str__()} with trunk size {self.trunk_size}L"

    def start_engine(self) -> str:
        """
        Запускает двигатель легкового автомобиля.

        :return: Сообщение о запуске двигателя с дополнительной информацией.
        """
        return f"{super().start_engine()} (Sedan specific message)"


class Truck(Car):
    """
    Класс для грузовых автомобилей, наследующий от Car.
    """

    def __init__(self, brand: str, model: str, year: int, load_capacity: int) -> None:
        """
        Инициализация грузового автомобиля.

        :param brand: Марка грузового автомобиля.
        :param model: Модель грузового автомобиля.
        :param year: Год выпуска грузового автомобиля.
        :param load_capacity: Грузоподъемность в килограммах.
        """
        super().__init__(brand, model, year)  # Вызов конструктора базового класса
        self.load_capacity = load_capacity  # Грузоподъемность

    def __str__(self) -> str:
        """
        Возвращает строковое представление грузового автомобиля.

        :return: Строка с информацией о грузовом автомобиле.
        """
        return f"{super().__str__()} with load capacity {self.load_capacity}kg"

    def start_engine(self) -> str:
        """
        Запускает двигатель грузового автомобиля.

        :return: Сообщение о запуске двигателя с дополнительной информацией.
        """
        return f"{super().start_engine()} (Truck specific message)"


# Пример использования классов
if __name__ == "__main__":
    sedan = Sedan("Toyota", "Camry", 2020, 500)
    truck = Truck("Volvo", "FH", 2019, 20000)

    print(sedan)  # Вывод информации о легковом автомобиле
    print(truck)  # Вывод информации о грузовом автомобиле

    print(sedan.start_engine())  # Запуск двигателя легкового автомобиля
    print(truck.start_engine())  # Запуск двигателя грузового автомобиля