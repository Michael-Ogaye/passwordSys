
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
        delete_account method deletes a  saved account from the list
        '''
        Users.user_list.remove(self)
    



#This is the the start of defination of anpther class(credentials)
class Credentials:
    """
    this is a blue print of crendetials object
    """
