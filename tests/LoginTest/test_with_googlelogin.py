import  pytest
import unittest
from page_class.LoginPage.google_page import GooglePage
from common_utils.teststatus import TestStatus
from base_utils.selenium_driver import SeleniumDriver

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class TestWithGoogle(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.sel = SeleniumDriver(self.driver)
        self.googleLogin=GooglePage(self.driver)
        self.result=TestStatus(self.driver)

    def test_google_login(self):
        status=self.googleLogin.loginWithGoogle("suryakanta@abacies.com","2357987")
        self.result.markFinal("test_google_login",status,"Sucessfull login verification")

    def tearDown(self):
        for method, error in self._outcome.errors:
            if error:
                # self.driver.get_screenshot_as_file("screenshot" + self.id() + ".png")
                self.sel.takeScreenShot("Taking the screen shot for "+str(method))