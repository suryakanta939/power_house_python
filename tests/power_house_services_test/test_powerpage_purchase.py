import unittest
import pytest
from time import sleep
from page_class.PaymentPage.cart_page import CartPage
from page_class.Power_house_service_page.power_house_service_page import PowerHouseServices
from page_class.Power_house_service_page.power_page import PowerPage
from page_class.LoginPage.google_page import GooglePage
from base_utils.selenium_driver import SeleniumDriver



@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class TestPowerPagePurchase(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.sel=SeleniumDriver(self.driver)
        self.lg=GooglePage(self.driver)
        self.ph=PowerHouseServices(self.driver)
        self.cp=CartPage(self.driver)
        self.pp=PowerPage(self.driver)

    def test_powerpage_purchase(self):
        self.lg.loginWithGoogle("suryakanta@abacies.com","9066549823")
        sleep(1)
        self.ph.mouseOverOnPowerhouseService()
        self.ph.clickOnPowerPage()
        self.pp.clickOnPowerPageAddTocart()
        sleep(3)
        self.pp.clickOnViewCart()
        self.cp.clickOnProceedCheckOut()
        self.pp.purchagePowerPage()


    def tearDown(self):
        for method, error in self._outcome.errors:
            if error:
                # self.driver.get_screenshot_as_file("screenshot" + self.id() + ".png")
                self.sel.takeScreenShot(str(method))


