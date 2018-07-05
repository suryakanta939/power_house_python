from base_utils.selenium_driver import SeleniumDriver
from time import sleep
from selenium.common.exceptions import *
class GooglePage(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)

    _login_google_xpath="//a[contains(@href,'https://accounts.google.com/')]"
    _heading_text_id="headingText"
    _email_field_id="identifierId"
    _next_button_xpath="//span[text()='Next']"
    _password_xpath="//input[@type='password']"
    _power_house_img_xpath="//img[contains(@src,'//storage.googleapis.com/staging-powerhouse-social/')]"

    def clickOnLoginWIthGoogle(self):
        self.clickOnElement("xpath",self._login_google_xpath)

    def enterEmailId(self,emailid):
        self.sendKeys("id",self._email_field_id,emailid)

    def clcikOnNextButton(self):
        self.clickOnElement("xpath",self._next_button_xpath)

    def enterPassWord(self,enterpassWord):
        self.sendKeys("xpath",self._password_xpath,enterpassWord)


    def loginWithGoogle(self,emailid,password):

            self.clickOnLoginWIthGoogle()
            sleep(2)
            self.waitForTheVisibilty(10, "id", self._heading_text_id)
            self.enterEmailId(emailid)
            self.clcikOnNextButton()
            sleep(2)
            self.waitForTheVisibilty(10, "xpath", self._password_xpath)
            self.enterPassWord(password)
            self.clcikOnNextButton()
            sleep(5)
            self.waitForTheVisibilty(10,"xpath",self._power_house_img_xpath)
            result=self.isElementPresent("xpath",self._power_house_img_xpath)
            if result==True:
                return result
            else:
                return result


