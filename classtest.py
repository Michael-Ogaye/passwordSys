import unittest
from main import Users
from main import Credentials

class Testuser(unittest.TestCase):
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

    def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list
        """
        self.new_user.adduser()
        self.assertEqual(len(Users.user_list),1)

class TestCreds(unittest.TestCase):
    """
    A test class that defines test cases for credentials class
    """ 
    def setUp(self):
        """
        Method that runs before each individual credentials test methods run.
        """
        self.new_credential = Credentials('uma','Ogaye Michael','beaut56')
    def test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credential.account,'uma')
        self.assertEqual(self.new_credential.userName,'Ogaye Michael')
        self.assertEqual(self.new_credential.password,'beaut56')

    


