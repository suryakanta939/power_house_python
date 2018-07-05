from base_utils.selenium_driver import SeleniumDriver
from time import  sleep

class TenMinutesMail(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)

    __mail_box_id="fe_text"
    _toactivate_message_xpath="//a[contains(text(),'Activate your account')]"
    _activation_link_xpath="//td[p[contains(text(),'Thanks for registering')]]//p[2]/a"
    _activation_message_xpath="//h1[@class='entry-title']"
    _login_link_xpath="//a[text()='log in']"

    count=0

    def getMail(self):
        mail=self.getElement("id",self.__mail_box_id).get_attribute("value")
        return mail


    def clickOnActivateMessage(self):
        self.clickOnElement("xpath",self._toactivate_message_xpath)


    def clickOnActivateLink(self):
        self.clickOnElement("xpath",self._activation_link_xpath)


    def getActiavtionMessage(self):
        message=self.getElement("xpath",self._activation_message_xpath).text
        return message

    def clickOnLoginLinkXpath(self):
        self.clickOnElement("xpath",self._login_link_xpath)

    def actiavteTheUser(self):
        while self.count<=10:
            try:
                self.waitForTheVisibilty(10, "xpath", self._toactivate_message_xpath)
                self.clickOnActivateMessage()
                self.waitForTheVisibilty(10, "xpath", self._activation_link_xpath)
                self.clickOnActivateLink()
                break
            except Exception as e:
                self.count+=1
                print(self.count)
                self.driver.refresh()
                sleep(3)

        self.handelWindowByNo(2)
        while True:
           try:
               self.waitForTheVisibilty(10, "xpath", self._activation_message_xpath)
               message = self.getActiavtionMessage()
               print(message)
               self.clickOnLoginLinkXpath()
               break
           except Exception as e:
               sleep(3)





