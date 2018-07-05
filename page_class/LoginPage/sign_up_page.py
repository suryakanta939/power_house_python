from base_utils.selenium_driver import SeleniumDriver
from page_class.LoginPage.tenminutes_mail_apge import TenMinutesMail
import names
from time import sleep


class SignUp(TenMinutesMail):

    def __init__(self,driver):
        super().__init__(driver)

    _sign_up_id="register-trigger"
    _username_id="reg-name"
    _email_id="reg-email"
    _password_id="reg-pass"
    _passWord_confirm_id="reg-pass-confirmation"
    _first_name_id="reg-fname"
    _last_name_id="reg-lname"
    _register_button_xpath_="//input[@name='reg_submit']"
    _registartion_sucessfull_message_xpath="//strong[contains(text(),'Registration complete.')]"

    _login_user_id="user"
    _login_password_id="pass"
    _login_submit_button_id="wp-submit"

    _power_house_img_xpath = "//img[contains(@src,'//storage.googleapis.com/staging-powerhouse-social/')]"
    count=0

    #**********Below xpath are for 10mins mail*************

    _mail_box_xpath="//input[@class='mailtext']"


    def clickOnSignUp(self):
        self.clickOnElement("id",self._sign_up_id)

    def enterUserName(self,username):
        self.sendKeys("id",self._username_id,username)

    def enterEmailId(self,email):
        self.sendKeys("id",self._email_id,email)

    def enterPassWord(self,password):
        self.sendKeys("id",self._password_id,password)

    def enterConfirmPassWord(self,confirm_password):
        self.sendKeys("id",self._passWord_confirm_id,confirm_password)

    def enterFirstName(self,first_name):
        self.sendKeys("id",self._first_name_id,first_name)

    def enterLastName(self,last_Name):
        self.sendKeys("id",self._last_name_id,last_Name)

    def clickOnRegisterButton(self):
        self.clickOnElement("xpath",self._register_button_xpath_)


    def fillingSignUpPage(self,email):
        while True:
            try:
                self.waitForTheVisibilty(10, "id", self._sign_up_id)
                self.clickOnSignUp()
                break
            except Exception as e:
                sleep(3)
        sleep(2)
        userName=names.get_first_name(gender="female")
        self.enterUserName(userName.lower()+"db")
        sleep(1)
        self.enterEmailId(email)
        sleep(1)
        self.enterPassWord("Surya.east09")
        sleep(1)
        self.enterConfirmPassWord("Surya.east09")
        sleep(1)
        # firstname = names.get_first_name(gender="male")
        # self.enterFirstName(firstname)
        # sleep(1)
        # lastName=names.get_last_name()
        # self.enterLastName(lastName)
        # sleep(1)
        self.clickOnRegisterButton()
        while self.count<=10:
            try:
                self.waitForTheVisibilty(10,"xpath",self._registartion_sucessfull_message_xpath)
                message=self.getElement("xpath",self._registartion_sucessfull_message_xpath).text
                print(message)
                break
            except Exception as e:
                self.count+=1
                print("waiting for the successfull message")
                sleep(3)

    def traDitonalLogin(self,username,password):

        self.sendKeys("id",self._login_user_id,username)
        self.sendKeys("id",self._login_password_id,password)
        self.clickOnElement("id",self._login_submit_button_id)
        sleep(5)
        self.waitForTheVisibilty(10, "xpath", self._power_house_img_xpath)
        result = self.isElementPresent("xpath", self._power_house_img_xpath)
        if result == True:
            return result
        else:
            return result
