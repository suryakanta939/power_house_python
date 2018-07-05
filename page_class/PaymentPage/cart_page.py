from base_utils.selenium_driver import SeleniumDriver

class CartPage(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)

    _cart_heading_xpath="//h1[text()='Cart']"
    _proceed_to_checkout_xpath="//a[contains(text(),'Proceed to checkout')]"


    def clickOnProceedCheckOut(self):
        self.waitForTheVisibilty(10,"xpath",self._cart_heading_xpath)
        if self.isElementPresent("xpath",self._proceed_to_checkout_xpath):
            self.clickOnElement("xpath",self._proceed_to_checkout_xpath)