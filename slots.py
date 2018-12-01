class TestClass:

    __slots__ = ['attr1', 'attr2', 'attr3']

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2


obj = TestClass(1, 2)
obj.attr1 = 5
obj.attr2 = 6
obj.attr3 = 7

# obj.atrr4 = 8
