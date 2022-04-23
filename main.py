
# This is the main module
import random
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
