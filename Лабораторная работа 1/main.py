from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make: str, model: str, year: int):
        """
        Инициализирует транспортное средство.

        :param make: Производитель транспортного средства (например, 'Toyota').
        :param model: Модель транспортного средства (например, 'Camry').
        :param year: Год выпуска транспортного средства (должен быть не меньше 1886).

        :raises ValueError: Если год выпуска меньше 1886.
        """
        if year < 1886:
            raise ValueError("Год выпуска не может быть меньше 1886.")
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start_engine(self) -> None:
        """
        Запускает двигатель транспортного средства.
        """
        ...

    @abstractmethod
    def stop_engine(self) -> None:
        """
        Останавливает двигатель транспортного средства.
        """
        ...

    @abstractmethod
    def drive(self) -> str:
        """
        Двигает транспортное средство.

        :return: Строка, описывающая движение транспортного средства.

        :doctest:
        >>> vehicle = Car('Toyota', 'Camry', 2020)
        >>> vehicle.drive()
        'Toyota Camry движется вперед.'
        """
        ...

    class Appliance(ABC):
        def __init__(self, brand: str, power: int):
            """
            Инициализирует бытовое устройство.

            :param brand: Бренд устройства (например, 'Samsung').
            :param power: Мощность устройства в ваттах (должна быть положительной).

            :raises ValueError: Если мощность меньше или равна 0.
            """
            if power <= 0:
                raise ValueError("Мощность должна быть положительной.")
            self.brand = brand
            self.power = power

        @abstractmethod
        def turn_on(self) -> None:
            """
            Включает устройство.
            """
            ...

        @abstractmethod
        def turn_off(self) -> None:
            """
            Выключает устройство.
            """
            ...

        @abstractmethod
        def get_power_consumption(self) -> int:
            """
            Возвращает мощность устройства.

            :return: Мощность в ваттах.

            :doctest:
            >>> appliance = WashingMachine('LG', 1500)
            >>> appliance.get_power_consumption()
            1500
            """
            ...

        class Building(ABC):
            def __init__(self, address: str, floors: int):
                """
                Инициализирует здание.

                :param address: Адрес здания (например, '123 Main St').
                :param floors: Количество этажей в здании (должно быть положительным).

                :raises ValueError: Если количество этажей меньше или равно 0.
                """
                if floors <= 0:
                    raise ValueError("Количество этажей должно быть положительным.")
                self.address = address
                self.floors = floors

            @abstractmethod
            def get_total_area(self) -> float:
                """
                Возвращает общую площадь здания.

                :return: Площадь в квадратных метрах.

                :doctest:
                >>> building = Skyscraper('456 High St', 50)
                >>> building.get_total_area()
                10000.0  # Пример возвращаемого значения
                """
                ...

            @abstractmethod
            def add_floor(self) -> None:
                """
                Добавляет этаж в здание.
                """
                ...

            @abstractmethod
            def remove_floor(self) -> None:
                """
                Удаляет этаж из здания.
                """
                ...