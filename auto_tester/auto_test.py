#!/usr/bin/env python3

from account_validate import Account, validate_user
import unittest
from faker import Faker #pip install Faker

fake = Faker()

class ValidateAccount(unittest.TestCase):
    def test_faker(self):
        testcase = Account(fake.first_name(), fake.last_name(), fake.bothify(text='(###) ###-####'))
        expected = 0
        self.assertEqual(validate_user(testcase), expected)

unittest.main()
  
