
from random import randint
import unittest






class TestPrivateKey(unittest.TestCase):
    def test_deterministic_k(self):
        pk = PrivateKey(randint(0, 10), 1)
        pk.deterministic_k(255)


if __name__ == '__main__':
    unittest.main()
