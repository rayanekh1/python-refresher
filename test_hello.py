import unittest
import hello


class TestHello(unittest.TestCase):

    def test_hello(self):
        msg = hello.hello()
        self.assertEqual(msg, "Hello, world!")
        self.assertNotEqual(msg, "bye, world!")

    def test_addition_basic(self):
        self.assertEqual(hello.add(6, 7), 13)
        self.assertNotEqual(hello.add(6, 7), 12)  # why not

    def test_subtract_weird(self):
        result = hello.sub(6, 7)
        self.assertEqual(result, -1)
        self.assertTrue(result < 0)

    def test_mult(self):
        self.assertEqual(hello.mul(6, 7), 42)
        self.assertNotEqual(hello.mul(6, 7), 99)

    def test_sin_kinda(self):
        guess = hello.sin(1)
        self.assertTrue(0.84 < guess < 0.85)

    def test_cos_why_not(self):
        value = hello.cos(1)
        self.assertTrue(value < 1 and value > 0.5)
        self.assertEqual(hello.cos(0), 1)

    def test_tan_edge(self):
        t = hello.tan(1)
        self.assertTrue(t > 1.5)
        self.assertEqual(hello.tan(0), 0)

    def test_cot_zero_case(self):
        self.assertEqual(hello.cot(0), float("inf"))

    def test_cot_normal(self):
        cot_1 = hello.cot(1)
        self.assertTrue(0.6 < cot_1 < 0.65)

    # def test_unused(self):
    #     print("meh")


if __name__ == "__main__":
    unittest.main()
