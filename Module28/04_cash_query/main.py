
class LRUCache:
    """Класс кэширования информации"""

    def __init__(self, cash_count: int) -> None:
        self.__cash_count = cash_count
        self.__cache = list()

    @property
    def cash_count(self) -> int:
        return self.__cash_count

    @cash_count.setter
    def cash_count(self, cash_count: int) -> None:
        self.__cash_count = cash_count

    @property
    def cache(self) -> list:
        return self.__cache

    @cache.setter
    def cache(self, new_elem: tuple) -> None:
        if len(self.cache) >= self.cash_count:
            self.cache.pop(0)
        self.cache.append(new_elem)

    def print_cache(self) -> None:
        print('LRU Cache:')
        for elem in self.cache:
            print(f'{elem[0]} : {elem[1]}')

    def get(self, key: str) -> str:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                result = self.cache.pop(i)
                self.cache.append(result)
                return result[1]


cache = LRUCache(3)
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")
cache.print_cache()
print(cache.get("key2"))
cache.cache = ("key4", "value4")
cache.print_cache()
