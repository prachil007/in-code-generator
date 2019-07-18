from random import randint


class NumberUtils:

    @staticmethod
    def random(n) -> int:
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)
