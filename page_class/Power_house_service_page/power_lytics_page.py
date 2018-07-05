from page_class.PaymentPage.payment_page import BillingDetails

class PowerLytics(BillingDetails):

    def __init__(self,driver):
        super().__init__(driver)

    _free_trial_lytics_add_cart="//a[@href='/subscriptions/?add-to-cart=160']"
    _view_cart_xpath = "//a[text()='View cart']"


    def clickOnFreeLyticsaddTocart(self):
        self.clickOnElement("xpath",self._free_trial_lytics_add_cart)


    def clickOnViewCartPowerLytics(self):
        self.waitForTheVisibilty(10,"xpath",self._view_cart_xpath)
        self.clickOnElement("xpath",self._view_cart_xpath)


    def purchasePowerLyticsFree(self):

        self.filliingUpBillingDetails()
        self.selectdirectBankTransferPayment()
        self.clickOnSubmit()
        self.waitingForThankYouMessage()
