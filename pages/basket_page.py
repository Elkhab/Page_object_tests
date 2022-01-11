from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        text_in_basket = self.browser.find_element(*BasketPageLocators.BASKET_INNER).text
        assert "Ваша корзина пуста" in text_in_basket



