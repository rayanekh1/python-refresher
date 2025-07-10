# test_bank_account.py

import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        # starting with $100 to mess with
        self.acc = BankAccount("Rayane Khoulani", "BWSI2025", 100.0)

    def test_deposit_valid(self):
        self.acc.deposit(25)
        self.assertEqual(self.acc.check_balance(), 125.0)

    def test_deposit_zero(self):
        with self.assertRaises(Exception):
            self.acc.deposit(0)

    def test_deposit_negative(self):
        with self.assertRaises(Exception):
            self.acc.deposit(-5)

    def test_withdraw_valid(self):
        self.acc.withdraw(40)
        self.assertEqual(self.acc.check_balance(), 60.0)

    def test_withdraw_too_much(self):
        with self.assertRaises(Exception):
            self.acc.withdraw(1000)

    def test_withdraw_zero(self):
        with self.assertRaises(Exception):
            self.acc.withdraw(0)

    def test_balance_rounding(self):
        weird = BankAccount("Test", "X123", 123.456789)
        self.assertEqual(weird.check_balance(), 123.46)

    def test_str_format(self):
        result = str(self.acc)
        self.assertIn("Rayane Khoulani", result)
        self.assertIn("BWSI2025", result)
        self.assertIn("100.00", result)


if __name__ == "__main__":
    unittest.main()
