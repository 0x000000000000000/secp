import unittest


class FieldElement:

    def __init__(self, num, prime):
        if num >= prime or num < 0:
            raise ValueError("invalid num")

        self.num = num
        self.prime = prime

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, other):
        if other == None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        if self.prime != other.prime:
            raise ValueError("invalid prime")

        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime:
            raise ValueError("invalid prime")
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, other):
        if self.prime != other.prime:
            raise ValueError("invalid prime")

        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)

    def __truediv__(self, other):
        if self.prime != other.prime:
            raise ValueError("invalid prime")
        num = (self.num * pow(other.num, self.prime - 2, self.prime)) % self.prime
        return self.__class__(num, self.prime)

    def __rmul__(self, coefficient):
        num = (self.num * coefficient) % self.prime
        return self.__class__(num, self.prime)


class TestFieldElement(unittest.TestCase):
    def test_fieldelement(self):
        f1 = FieldElement(3, 31)
        f2 = FieldElement(24, 31)
      #   print(f1 == f2)
      #   print(f1 != f2)
      #   print("add", (f1 + f2).num)
      #   print("sub", (f1 - f2).num)
      #   print("mul", (f1 * f2).num)
      #   print("div", (f1 / f2).num)
      #   print("pow", (f1 ** 2).num)
        a = FieldElement(17, 31)
        b = FieldElement(21, 31)
        print(a+b)

        a = FieldElement(24, 31)
        b = FieldElement(19, 31)

        print("a*b", a*b)
        a = FieldElement(17, 31)
        b = a**3
        print(b)
        a = FieldElement(5, 31)
        b = FieldElement(18, 31)
        c = a**5 * b
        print(c)


if __name__ == '__main__':
    unittest.main()
