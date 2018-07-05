import pytest
import unittest
from page_class.LoginPage.sign_up_page import SignUp
from base_utils.selenium_driver import SeleniumDriver
from page_class.LoginPage.tenminutes_mail_apge import TenMinutesMail
from time import sleep
from page_class.LoginPage.google_page import GooglePage

@pytest.mark.userfixtures("oneTimeSetUp","setUp")
class TestSignUp(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.sel = SeleniumDriver(self.driver)
        self.ten=TenMinutesMail(self.driver)
        self.su=SignUp(self.driver)

    def test_signup(self):
        self.driver.get("https://10minutemail.net/")
        mail=self.ten.getMail()
        print("the mail is "+mail)
        self.sel.openNewTab("https://app.pohostaging.com/login/")
        self.sel.handelWindowByNo(2)
        self.su.fillingSignUpPage(mail)
        self.driver.close()
        self.sel.handelWindowByNo(1)
        self.su.actiavteTheUser()
        self.su.traDitonalLogin(mail,"Surya.east09")






    def tearDown(self):
        for method, error in self._outcome.errors:
            if error:
                # self.driver.get_screenshot_as_file("screenshot" + self.id() + ".png")
                self.sel.takeScreenShot(str(method))