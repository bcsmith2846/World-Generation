from generators import simple_generator
import unittest
from random import Random

class Test_SimpleGenerator(unittest.TestCase):
    def test_simplegen_add(self):
        gen = simple_generator.SimpleGenerator()
        rand = Random()
        for x in range(10000):
            a = rand.randint(-10000,10000)
            b = rand.randint(-10000,10000)
            self.assertEqual(a+b,gen.add(a,b))

if __name__ == '__main__':
    unittest.main()
