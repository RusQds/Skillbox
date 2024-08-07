import os
from typing import TextIO, Optional


class File:
    """Контекст менеджер File"""

    def __init__(self, my_file: str, mode: str) -> None:
        self.__path = os.path.abspath(my_file)
        self.__file = None
        self.__mode = mode

    @property
    def path(self) -> str:
        return self.__path

    @property
    def mode(self) -> str:
        return self.__mode

    @property
    def file(self) -> Optional[TextIO]:
        return self.__file

    @mode.setter
    def mode(self, mode: str) -> None:
        self.__mode = mode

    @path.setter
    def path(self, path: str) -> None:
        self.__path = path

    @file.setter
    def file(self, my_file: str) -> None:
        self.__file = my_file

    def __enter__(self) -> TextIO:
        #при попытке открыть несуществующий файл, менеджер автоматически создаёт и открывает этот файл в режиме записи.
        if not os.path.exists(self.path):
            self.mode = 'a'
        self.file = open(self.path, self.mode, encoding='utf-8')
        return self.file

    def __exit__(self, type, value, traceback) -> bool:
        self.file.close()
        #На выходе из менеджера подавляются все исключения, связанные с файлами.
        if type is IOError:
            return True


with File('file.txt', 'r') as file:
    if file.mode in ('w', 'a'):
        my_text = input('Введите текст: ')
        file.write(my_text)
    else:
        print(file.read())
