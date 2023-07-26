import unittest
import field


class Point:
    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.x is None and self.y is None:
            return
        if self.y ** 2 != self.x ** 3 + a*x + b:
            raise ValueError("invalid params")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise ValueError("invalid params")

        if self.x is None:
            return other

        if other.x is None:
            return self

        if self.x == other.x and self.y != self.y:
            return self.__class__(None, None, self.a, self.b)

        if self.x != other.x:
            s = (other.y-self.y)/(other.x - self.x)
            x = s**2 - self.x-other.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)

        if self == other and self.y == 0 * self.x:
            return self.__class__(None, None, self.a, self.b)

        if self == other:
            s = (3 * self.x**2 + self.a) / (2 * self.y)
            x = s**2 - 2 * self.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)

    def __rmul__(self, coefficient):
        coef = coefficient
        current = self
        result = self.__class__(None, None, self.a, self.b)
        while coef:
            if coef & 1:
                result += current
            current += current
            coef >>= 1

        return result


class TestPoint(unittest.TestCase):
    def test_point(self):
        # p1 = Point(2, 5, 5, 7)
        # p2 = Point(2, -5, 5, 7)
        # print(p1 == p2)
        # print(p1 != p2)
        # print(p1 + p2)

        prime = 223
        a = field.FieldElement(0, prime)
        b = field.FieldElement(7, prime)

        f1 = field.FieldElement(192, prime)
        f2 = field.FieldElement(105, prime)

        f3 = field.FieldElement(17, prime)
        f4 = field.FieldElement(56, prime)

        p1 = Point(f1, f2, a, b)
        p2 = Point(f3, f4, a, b)

        a = field.FieldElement(24, 31)
        b = 2
        print(b*a, a+a)


if __name__ == '__main__':
    unittest.main()
