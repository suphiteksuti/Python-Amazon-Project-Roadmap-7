from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Actions:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, driver, selector):
        return WebDriverWait(driver, 5).until(ec.element_to_be_clickable(selector))

    def input(self,element, input):
        WebDriverWait(self.driver, 70).until(EC.presence_of_element_located((By.NAME, element))) \
            .send_keys(input)

    def click(self, element, loc):
        if (loc == "ID"):
            selectedElement = (By.ID, element)
            delay = WebDriverWait(self.driver, 70).until(EC.element_to_be_clickable(selectedElement))
            delay.click()
        else:
            selectedElement = (By.XPATH, element)
            delay = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(selectedElement))
            delay.click()

    def text(self, element):
        text = self.driver.find_element_by_xpath(element).text
        return text