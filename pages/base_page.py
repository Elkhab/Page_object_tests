from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math
from pages.locators import BasePageLocators
from pages import ProductPageLocators





class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)



    def open(self):
        self.browser.get(self.url)

        def is_element_present(self, how, what):
            try:
                self.browser.find_element(how, what)
            except (NoSuchElementException):
                return False
            return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"









    def add_product_to_basket(self):
        basket = self.browser.find_element(
                    *ProductPageLocators.MainPageLocators.BASKET)
        basket.click()





    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")




    def should_be_book_added(self):
                message_basket_total = self.browser.find_element(
                    *ProductPageLocators.MainPageLocators.CART_PRICE)
                product_price = self.browser.find_element(
                    *ProductPageLocators.MainPageLocators.PRODUCT_PRICE)
                print(product_price.text)
                print(message_basket_total.text)



            #assert product_price.text == message_basket_total.text, "не равно"