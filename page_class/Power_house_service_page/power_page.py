from base_utils.selenium_driver import SeleniumDriver
from page_class.PaymentPage.payment_page import BillingDetails
from time import sleep

class PowerPage(BillingDetails):
    def __init__(self,driver):
        super().__init__(driver)

    _add_to_cart_xpath="//a[text()='Add To Cart']"
    _view_cart_xpath = "//a[text()='View cart']"
    # here the view cart path chnaged
    def clickOnPowerPageAddTocart(self):
        self.clickOnElement("xpath",self._add_to_cart_xpath)

    def clickOnViewCart(self):
        self.waitForTheVisibilty(10,"xpath",self._view_cart_xpath)
        self.clickOnElement("xpath",self._view_cart_xpath)

    def purchagePowerPage(self):
        self.filliingUpBillingDetails()
        self.selectdirectBankTransferPayment()
        self.clickOnSubmit()
        self.waitingForThankYouMessage()