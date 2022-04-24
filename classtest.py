import unittest
from main import Users
from main import Credentials

class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = Users('OgayeMike','yuvicytr')
    
    def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username,'OgayeMike')
        self.assertEqual(self.new_user.password,'yuvicytr')

