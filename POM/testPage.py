import unittest
from selenium import webdriver
from POM.PAGES.homePage import MainPage
from POM.PAGES.searchPage import SearchPage
from POM.PAGES.productPage import ProductPage
from POM.PAGES.loginPage import LoginPage

class testAmazon(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.chrome()
        self.driver.get("https://www.amazon.com")
        self.driver.maximize_window()

    def runTest(self):
        main_page = MainPage(self.driver)
        login_page = LoginPage(self.driver)
        search_page = SearchPage(self.driver)
        product_page = ProductPage(self.driver)
        main_page.check_page()
        main_page.login_button()
        login_page.sign_button()
        login_page.email()
        login_page.password()
        login_page.submit()
        search_page.Search()
        search_page.check_results()
        search_page.click_pagination()
        search_page.check_2_pagination()
        search_page.select_product()
        product_page.add_to_List()
        product_page.wish_list()
        product_page.check_product()
        product_page.delete_wishlist()
        product_page.wish_list()



