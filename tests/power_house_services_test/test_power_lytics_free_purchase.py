import pytest
import unittest
from time import sleep
from page_class.LoginPage.google_page import GooglePage
from page_class.Power_house_service_page.power_house_service_page import PowerHouseServices
from page_class.Power_house_service_page.power_lytics_page import PowerLytics
from page_class.PaymentPage.cart_page import CartPage
from base_utils.selenium_driver import SeleniumDriver


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class TestPowerLyticsPurchase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.sel=SeleniumDriver(self.driver)
        self.gg=GooglePage(self.driver)
        self.ph=PowerHouseServices(self.driver)
        self.pl=PowerLytics(self.driver)
        self.cp=CartPage(self.driver)

    def test_Power_power_mail(self):
        self.gg.loginWithGoogle("suryakanta@abacies.com","9066549823")
        sleep(2)
        self.ph.mouseOverOnPowerhouseService()
        self.ph.clickOnPowerLytics()
        self.pl.clickOnFreeLyticsaddTocart()
        sleep(3)
        self.pl.clickOnViewCartPowerLytics()
        self.cp.clickOnProceedCheckOut()
        self.pl.purchasePowerLyticsFree()

    def tearDown(self):
        for method,error in self._outcome.errors:
            if error:
                self.sel.takeScreenShot(str(method))

