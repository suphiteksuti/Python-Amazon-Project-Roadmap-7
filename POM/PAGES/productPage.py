from POM.locators import Locators
from POM.actions import Actions

class ProductPage(Actions):

    def add_to_List(self):
        Actions.click(Locators.ADD_LIST, 'NAME')

    def wish_list(self):
        Actions.click(Locators.WISH_LIST, 'LINK_TEXT')

    def check_product(self):
        assert Locators.SELECT_PRODUCT in Locators.WISH_LIST_PRODUCT

    def delete_wishlist(self):
        Actions.click(Locators.DELETE_WISHLIST, 'LINK_TEXT')

    def check_wishlist(self):
        assert "0 items in this view" in Actions.text(Locators.CHECK_WISHLIST)
