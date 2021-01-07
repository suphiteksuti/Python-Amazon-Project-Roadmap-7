from POM.locators import Locators
from POM.actions import Actions

class SearchPage(Actions):

    def Search(self):
        Actions.input(Locators.SEARC_AREA, 'Samsung')

    def click_pagination(self):
        Actions.click(Locators.PAGINATION, 'LINK_TEXT')

    def check_results(self):
        assert "1-16 of over 2,000 results for" in Actions.text(Locators.CHECK_RESULTS)

    def check_2_pagination(self):
        assert "17-32 of over 10,000 results for" in Actions.text(Locators.CHECK_RESULTS)

    def select_product(self):
        Actions.click(Locators.SELECT_PRODUCT, 'ID')
