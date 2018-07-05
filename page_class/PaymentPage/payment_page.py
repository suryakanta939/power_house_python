from builtins import print

from base_utils.selenium_driver import SeleniumDriver
import names
from time import sleep

class BillingDetails(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)

    _first_name_id="billing_first_name"
    _last_name_id="billing_last_name"
    _company_name_id="billing_company"
    _country_name_id="billing_country"
    _street_adress1_id="billing_address_1"
    _street_adress2_id = "billing_address_2"
    _city_id="billing_city"
    _state_id="billing_state"
    _post_code_id="billing_postcode"
    _phone_id="billing_phone"
    _email_id="billing_email"
    _direct_bank_radio_xpath="//input[@id='payment_method_bacs']"
    _terms_xpath="//input[@id='terms']"
    _submit_button_xpath="//button[@value='Submit']"
    _thank_you_message_xpath="//h1[text()='Thank You']"

    count=0
    thankYou=0
    def enterFirstName(self,firstName):
        self.getElement("id",self._first_name_id).clear()
        sleep(0.5)
        self.sendKeys("id",self._first_name_id,firstName)

    def enterLastName(self,lastName):
        self.getElement("id", self._last_name_id).clear()
        sleep(0.5)
        self.sendKeys("id",self._last_name_id,lastName)

    def enterCompanyName(self,comapnyName):
        self.getElement("id", self._company_name_id).clear()
        sleep(0.5)
        self.sendKeys("id", self._company_name_id, comapnyName)

    def selectCountryName(self,countryName):
        self.selectByText("id",self._country_name_id,countryName)

    def enterStreetAdressOne(self,address1):
        self.getElement("id", self._street_adress1_id).clear()
        sleep(0.5)
        self.sendKeys("id", self._street_adress1_id, address1)

    def enterStreetAdressTwo(self,address2):
        self.getElement("id", self._street_adress2_id).clear()
        sleep(0.5)
        self.sendKeys("id",self._street_adress2_id,address2)

    def enterCityName(self,cityName):
        self.getElement("id", self._city_id).clear()
        sleep(0.5)
        self.sendKeys("id",self._city_id,cityName)

    def selectState(self,stateName):
        self.selectByValue("id",self._state_id,stateName)

    def enterPostCode(self,postcode):
        self.getElement("id", self._post_code_id).clear()
        sleep(0.5)
        self.sendKeys("id",self._post_code_id,postcode)

    def enterPhoneNo(self,phoneNo):
        self.getElement("id", self._phone_id).clear()
        sleep(0.5)
        self.sendKeys("id",self._phone_id,phoneNo)

    def enterEmailId(self,email):
        self.getElement("id", self._email_id).clear()
        sleep(0.5)
        self.sendKeys("id",self._email_id,email)

    def clickOnDirectBankTransfer(self):
        self.clickOnElement("xpath",self._direct_bank_radio_xpath)

    def clickOntermsAndCondition(self):
        self.clickOnElement("xpath",self._terms_xpath)

    def clickOnSubmit(self):
        # self.moveToCordinateOfElement("xpath", self._submit_button_xpath)
        self.scrollToElement("xpath", self._submit_button_xpath)
        sleep(1)
        self.mouseHoverOnElement("xpath", self._submit_button_xpath)
        self.clickOnElement("xpath", self._submit_button_xpath)

    def readingTheThankYouMessage(self):
        messsage=self.getElement("xpath",self._thank_you_message_xpath).text
        return messsage

    def filliingUpBillingDetails(self):

        firstName=names.get_first_name(gender="male")
        self.enterFirstName(firstName)

        lastName=names.get_last_name()
        self.enterLastName(lastName)

        self.enterCompanyName("abacies logiciels pvt ltd")

        self.selectCountryName("New Zealand")
        self.enterStreetAdressOne("hal 2 phase")
        self.enterStreetAdressTwo("behaind leela palace")
        self.enterCityName("Auckland")
        self.selectState("CT")
        self.enterPostCode("4983")
        self.enterPhoneNo("0123456789")
        self.enterEmailId("hello@gmail.com")

    def isDirectBankIsChecked(self):

        bank_check_box=self.getElement("xpath",self._direct_bank_radio_xpath)

        if bank_check_box.is_selected():
            return True
        else:
            return False

    def selectdirectBankTransferPayment(self):
        while self.count<=20:
            try:
                result=self.isDirectBankIsChecked()
                print("the buton is checked "+str(result))
                if result==True:
                    self.clickOntermsAndCondition()
                    print("clicked on the terms and condition as the bank is choosed already")
                    break
                else:
                    self.clickOnDirectBankTransfer()
                    self.clickOntermsAndCondition()
                    print("clciked on the terms and condition and also the bank type")
                    break
            except Exception as e:
                self.waitForTheVisibilty(10,"xpath",self._direct_bank_radio_xpath)
                sleep(3)
                print("waiting for the element to be visible")
                self.count += 1
                print(self.count)


    def waitingForThankYouMessage(self):
        while self.thankYou <=20:
            try:
                self.waitForTheVisibilty(10, "xpath", self._thank_you_message_xpath)
                result=self.readingTheThankYouMessage()
                print(result)
                break
            except Exception as e:
                self.thankYou+=1
                print("waiting for the Thank you message")
                sleep(3)





    def purchasingPowersite(self):
        self.filliingUpBillingDetails()
        self.selectdirectBankTransferPayment()
        self.clickOnSubmit()
        self.waitingForThankYouMessage()
