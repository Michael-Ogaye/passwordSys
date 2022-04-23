
# This is the main module
import random
import pyperclip
import string




class Users:
    """
    This class creates new instances of the user
    """

    user_list=[]
    def __init__(self,username,password):
        """
        This is the users constructor it creates new instances of the user
        """

        self.username=username
        self.password=password

    def adduser (self):
        """
        saves the usesrs entry to the users list
        """
       
        self.user_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        '''
        delete_account method deletes a  user
        '''
        Users.user_list.remove(self)
    



#This is the the start of defination of anpther class(credentials)
class Credentials:
    """
    this is a blue print of crendetials object
    """
    credslist=[]
    @classmethod
    def verify_user(cls,username, password):
        """
        method to verify whether the user is in our user_list or not
        """
        a_user = ""
        for user in Users.user_list:
            if(user.username == username and user.password == password):
                    a_user == user.username
        return a_user

    def __init__(self,account,userName, password):
        """
        instantiation of the credential class object
        """
        self.account = account
        self.userName = userName
        self.password = password

    def save_details(self):
        """
        method to store a new credential to the credslist
        """
        Credentials.credslist.append(self)

    def delete_credentials(self):
        """
        removes the users credentials when called
        """
        Credentials.credslist.remove(self)

    @classmethod
    def find_credential(cls, account):
        """
        Method that takes in a account_name and returns a credential that matches that account
        """
        for cred in cls.credslist:
            if cred.account == account:
                return cred
    @classmethod
    def copy_password(cls,account):
        found_credentials = Credentials.find_credential(account)
        pyperclip.copy(found_credentials.password)
    
    @classmethod
    def if_credential_exist(cls, account):
        """
        Method that checks if a credential exists from the credential list and returns true or false depending if the credential exists.
        """
        for cred in cls.credslist:
            if cred.account == account:
                return True
            else:   
                return False
    
    @classmethod
    def display_credentials(cls):
        """
        Method that returns all items in the credentials list
        """
        return cls.credslist

    def generatePassword(stringLength=9):
        
        """Generate a random password string of letters and digits and special characters"""
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "k&%)@#$"
        return ''.join(random.choice(password) for i in range(stringLength))

