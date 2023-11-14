import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):

    def test1(self):
        pwd = ""
        expected = False
        self.assertFalse(check_pwd(pwd), expected)

    def test2(self):
        pwd = "1234567"
        expected = False
        self.assertFalse(check_pwd(pwd), expected)

    def test3(self):
        pwd = "123456789012345678901"
        expected = False
        self.assertFalse(check_pwd(pwd), expected)

    def test4(self):
        pwd = "12345678a"
        expected = False
        self.assertFalse(check_pwd(pwd), expected)

    def test5(self):
        pwd = "12345678aB"
        expected = False
        self.assertFalse(check_pwd(pwd), expected)

if __name__ == '__main__':
    unittest.main()
