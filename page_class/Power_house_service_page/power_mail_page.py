from page_class.PaymentPage.payment_page import BillingDetails

class PowerMail(BillingDetails):

    def __init__(self,driver):
        super().__init__(driver)

    _free_trial_mail_add_cart="//a[@href='/subscriptions/?add-to-cart=152']"
    _view_cart_xpath = "//a[text()='View cart']"


    def clickOnFreemailaddTocart(self):
        self.clickOnElement("xpath",self._free_trial_mail_add_cart)


    def clickOnViewCartPowerMail(self):
        self.waitForTheVisibilty(10,"xpath",self._view_cart_xpath)
        self.clickOnElement("xpath",self._view_cart_xpath)


    def purchasePowerMailFree(self):

        self.filliingUpBillingDetails()
        self.selectdirectBankTransferPayment()
        self.clickOnSubmit()
        self.waitingForThankYouMessage()
