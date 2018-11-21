
class SquareIterator:

    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration

        result = self.current ** 2
        self.current += 1
        return result


for num in SquareIterator(2, 6):
    print(num)

