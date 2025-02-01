''' Write a scenario where a `UserAuthentication` interface contains `login()` and `logout()` methods, and it is implemented by `GoogleAuth` 
    and `FacebookAuth` classes.'''

from abc import ABC,abstractmethod
class UserAuthentication(ABC):
    @abstractmethod
    def login():
        pass
    @abstractmethod
    def logout():
        pass
class GoogleAuth(UserAuthentication):
    password='user@123'
    def login(self):
        print("Email and password is required to login")
        if GoogleAuth.password==input("Enter password : "):
            print("Login successful")
    def logout(self):
        print("Click logout button to exit from google")
class FacebookAuth(UserAuthentication):
    password1='textuser123'
    def login(self):
        print("Email and password is required to login")
        if FacebookAuth.password1==input("Enter password : "):
            print("Login successful")
    def logout(self):
        print("Click logout button to exit from facebook")
google=GoogleAuth()
google.login()
google.logout()
facebook=FacebookAuth()
facebook.login()
facebook.logout()