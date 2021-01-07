from POM.locators import Locators
from POM.actions import Actions

class LoginPage(Actions):

    def sign_button(self):
        Actions.click(Locators.SIGN_BUTTON, 'ID')

    def submit(self):
        Actions.click(Locators.SUBMIT, 'CLASS_NAME')

    def email(self):
        Actions.input(Locators.EMAIL, 'test@mail.com')

    def password(self):
        Actions.input(Locators.PASSWORD, '123456')
