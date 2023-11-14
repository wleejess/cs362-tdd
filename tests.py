import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):

    def test1(self):
        pwd = ""
        self.assertFalse(check_pwd(pwd))

if __name__ == '__main__':
    unittest.main()
