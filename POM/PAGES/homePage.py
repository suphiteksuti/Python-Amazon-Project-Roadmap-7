from POM.locators import Locators
from POM.actions import Actions

class MainPage(Actions):

    def check_page(self):
        assert "https://www.amazon.com/" in self.driver.current_url

    def login_button(self):
        Actions.click(Locators.LOGIN_BUTTON, 'ID')

    def search_button(self):
        Actions.click(Locators.SEARCH_BUTTON, 'CLASS_NAME')
