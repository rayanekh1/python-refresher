import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # starting with $100 to mess with
        self.acc = BankAccount("Rayane Khoulani", "BWSI2025", 100.0)

    def test_deposit_valid(self):
        """deposit a regular amount and check balance"""
        self.acc.deposit(25)
        self.assertAlmostEqual(self.acc.check_balance(), 125.0)
        self.assertNotAlmostEqual(self.acc.check_balance(), 124.99)

    def test_deposit_zero(self):
        """0 deposit shouldn’t work"""
        with self.assertRaises(Exception):
            self.acc.deposit(0)

    def test_deposit_negative(self):
        """no way u can deposit negative"""
        with self.assertRaises(Exception):
            self.acc.deposit(-5)

    def test_withdraw_valid(self):
        """take some money out and check"""
        self.acc.withdraw(40)
        self.assertEqual(self.acc.check_balance(), 60.0)

    def test_withdraw_too_much(self):
        """try robbing the bank"""
        with self.assertRaises(Exception):
            self.acc.withdraw(1000)

    def test_withdraw_zero(self):
        """withdrawing $0 shouldn’t do anything"""
        with self.assertRaises(Exception):
            self.acc.withdraw(0)

    def test_balance_rounding(self):
        """float precision check if it rounds it right"""
        weird = BankAccount("Test", "X123", 123.456789)
        self.assertEqual(weird.check_balance(), 123.46)

    def test_str_format(self):
        """check string printout thingy"""
        result = str(self.acc)
        self.assertIn("Rayane Khoulani", result)
        self.assertIn("BWSI2025", result)
        self.assertIn("100.00", result)
        self.assertNotIn("meow", result)

    def test_deposit_random_stuff(self):
        """should not accept weird deposits"""
        result1 = self.acc.deposit("pizza")
        result2 = self.acc.deposit(-50000)
        self.assertEqual(result1, False)
        self.assertEqual(result2, False)
        self.assertAlmostEqual(self.acc.check_balance(), 100.0)

    def test_withdraw_random_stuff(self):
        """should not let random bad stuff thru"""
        result1 = self.acc.withdraw("tacos")
        result2 = self.acc.withdraw(-9999)
        self.assertEqual(result1, False)
        self.assertEqual(result2, False)
        self.assertAlmostEqual(self.acc.check_balance(), 100.0)

    def test_display_format(self):
        """make sure display() looks like something a human would understand"""
        self.assertEqual(
            self.acc.display(), "Rayane Khoulani's account has a balance of $100.0"
        )


if __name__ == "__main__":
    unittest.main()
