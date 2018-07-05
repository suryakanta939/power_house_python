import pytest
import unittest
from time import sleep
from page_class.LoginPage.google_page import GooglePage
from page_class.Power_house_service_page.power_house_service_page import PowerHouseServices
from page_class.Power_house_service_page.power_mail_page import PowerMail
from page_class.PaymentPage.cart_page import CartPage
from base_utils.selenium_driver import SeleniumDriver


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class TestPowerMailPurchase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.sel=SeleniumDriver(self.driver)
        self.gg=GooglePage(self.driver)
        self.ph=PowerHouseServices(self.driver)
        self.pm=PowerMail(self.driver)
        self.cp=CartPage(self.driver)

    def test_Power_power_mail(self):
        self.gg.loginWithGoogle("suryakanta@abacies.com","9066549823")
        sleep(2)
        self.ph.mouseOverOnPowerhouseService()
        self.ph.clickOnPowerMail()
        self.pm.clickOnFreemailaddTocart()
        sleep(3)
        self.pm.clickOnViewCartPowerMail()
        self.cp.clickOnProceedCheckOut()
        self.pm.purchasePowerMailFree()

    def tearDown(self):
        for method,error in self._outcome.errors:
            if error:
                self.sel.takeScreenShot(str(method))

