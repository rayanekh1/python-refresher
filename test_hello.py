import unittest
import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertNotEqual(hello.hello(), "Hello, world!")


def test_add(self):
    self.assertEqual(hello.add(2, 3), 5)
    self.assertEqual(hello.add(-1, 1), 0)
    self.assertEqual(hello.add(0, 0), 0)


def test_mul(self):
    self.assertEqual(hello.mul(1, 5), 5)
    self.assertEqual(hello.mul(-2, 5), -10)
    self.assertEqual(hello.mul(0, 99), 0)


def test_sub(self):
    self.assertEqual(hello.sub(5, 3), 2)
    self.assertEqual(hello.sub(3, 5), -2)
    self.assertEqual(hello.sub(0, 0), 0)


def test_div(self):
    self.assertEqual(hello.div(10, 2), 5)
    self.assertAlmostEqual(hello.div(7, 3), 2.3333, places=4)
    with self.assertRaises(ValueError):
        hello.div(1, 0)


def test_div(self):
    self.assertEqual(hello.div(10, 2), 5)
    self.assertAlmostEqual(hello.div(1, 3), 0.3333333333, places=5)
    with self.assertRaises(ValueError):
        hello.div(1, 0)


def test_power(self):
    self.assertEqual(hello.power(2, 3), 8)
    self.assertEqual(hello.power(5, 0), 1)
    self.assertEqual(hello.power(2, 1), 2)


def test_sqrt(self):
    self.assertEqual(hello.sqrt(4), 2)
    self.assertEqual(hello.sqrt(0), 0)
    self.assertAlmostEqual(hello.sqrt(2), 1.4142, places=4)


def test_log(self):
    self.assertAlmostEqual(hello.log(np.e), 1, places=5)
    self.assertEqual(hello.log(1), 0)
    self.assertAlmostEqual(hello.log(10), 2.3025, places=4)


def test_exp(self):
    self.assertAlmostEqual(hello.exp(1), np.e, places=5)
    self.assertEqual(hello.exp(0), 1)
    self.assertAlmostEqual(hello.exp(2), 7.3891, places=4)


def test_cos(self):
    self.assertEqual(hello.cos(0), 1)
    self.assertEqual(hello.cos(1), 0.5403023058681398)


def test_sin(self):
    self.assertEqual(hello.sin(0), 0)
    self.assertAlmostEqual(hello.sin(np.pi / 2), 1, places=5)
    self.assertAlmostEqual(hello.sin(np.pi), 0, places=5)


def test_tan(self):
    self.assertEqual(hello.tan(0), 0)
    self.assertEqual(hello.tan(1), 1.5574077246549023)
    self.assertAlmostEqual(hello.tan(np.pi), 0, places=4)


def test_cos(self):
    self.assertEqual(hello.cos(0), 1)
    self.assertAlmostEqual(hello.cos(np.pi / 2), 0, places=5)
    self.assertAlmostEqual(hello.cos(np.pi), -1, places=5)


def test_cot(self):
    self.assertEqual(hello.cot(0), float("inf"))
    self.assertEqual(hello.cot(1), 0.6420926159343306)
    self.assertAlmostEqual(hello.cot(np.pi / 4), 1, places=5)


if __name__ == "__main__":
    unittest.main()
