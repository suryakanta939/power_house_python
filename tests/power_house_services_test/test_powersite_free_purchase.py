from page_class.LoginPage.google_page import GooglePage
from page_class.Power_house_service_page.power_site_page import PowerSitePage
from page_class.PaymentPage.cart_page import CartPage
from page_class.PaymentPage.payment_page import BillingDetails
import unittest
import pytest
from time import sleep
from base_utils.selenium_driver import SeleniumDriver


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class TestPowerservicespowerSite(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.sel = SeleniumDriver(self.driver)
        self.google=GooglePage(self.driver)
        self.ps=PowerSitePage(self.driver)
        self.cp=CartPage(self.driver)
        self.bd=BillingDetails(self.driver)


    def test_powersite_Purchase(self):
        self.google.loginWithGoogle("suryakanta@abacies.com","9066549823")
        sleep(1)
        self.ps.clickOnFreeTrialXpath()
        sleep(3)
        self.ps.clickOnViewCart()
        self.cp.clickOnProceedCheckOut()
        self.bd.purchasingPowersite()

    def tearDown(self):
        for method, error in self._outcome.errors:
            if error:

                self.sel.takeScreenShot(str(method))

