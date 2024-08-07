
class Date:
    """Класс обработки даты"""
    def __init__(self) -> None:
        self.__date_dict = {"d": None, "m": None, "y": None}

    def __str__(self) -> str:
        return f'День: {self.__date_dict["d"]}	Месяц: {self.__date_dict["m"]}	Год: {self.__date_dict["y"]}'

    @property
    def date_dict(self) -> dict:
        return self.__date_dict

    @date_dict.setter
    def date_dict(self, date_string: str) -> None:
        self.__date_dict["d"] = int(date_string.split('-')[0])
        self.__date_dict["m"] = int(date_string.split('-')[1])
        self.__date_dict["y"] = int(date_string.split('-')[2])

    @classmethod
    def from_string(cls, date_string: str) -> 'Date':
        if cls.is_date_valid(date_string):
            instance = cls()
            instance.date_dict = date_string
            return instance
        else:
            raise ValueError(f'Invalid date string: {date_string}')

    @classmethod
    def is_date_valid(cls, date_string: str) -> bool:
        if 1 <= int(date_string.split('-')[0]) <= 31 and 1 <= int(date_string.split('-')[1]) <= 12:
            return True
        else:
            return False


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

#Добавлена проверка на корректность даты при инициализации инстанса и выброс исключения
date_test = Date.from_string('32-12-2077')
