import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):

    def test1(self):
        pwd = ""
        expected = False
        self.assertFalse(check_pwd(pwd), expected)


if __name__ == '__main__':
    unittest.main()
