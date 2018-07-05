from page_class.DashBoard.dash_board_page import DashBoard

class AdminDashBoard(DashBoard):

    def __init__(self,driver):
        super().__init__(driver)

    _admin_home_xpath="//h3[contains(text(),'Home')]"
    _mysites_xpath="//h3[contains(text(),'My Sites')]"
    _domains_xpath="//h3[contains(text(),'Domains')]"
    _create_site_xpath="//h3[contains(text(),'Create Site')]"
    _option_form_xpath="//h3[contains(text(),'Optin Forms')]"
    _gloabal_setting_xpath="//h3[contains(text(),'Global settings')]"
    _persional_dasboard_xpath="//h3[contains(text(),'Personal DashBoard')]"
    _power_page_xpath="//h3[contains(text(),'PowerPages')]"
    _power_mail_unlcok_xpath="//a[@href='https://shop.pohostaging.com/subscriptions/#contacts']//i[@style='display:block;']"
    _power_lytcis_unlock_xpath="//a[@href='https://shop.pohostaging.com/subscriptions/#powerboards']//i[@style='display:block;']"


    def clickOnAdminHomePage(self):
        self.clickOnElement("xpath",self._admin_home_xpath)

    def clickOnmySites(self):
        self.clickOnElement("xpath",self._mysites_xpath)

    def clickOnDomain(self):
        self.clickOnElement("xpath",self._domains_xpath)

    def clickOnCreateSite(self):
        self.clickOnElement("xpath",self._create_site_xpath)

    def clickOnOptionForm(self):
        self.clickOnElement("xpath",self._option_form_xpath)

    def clickOnGlobalSetting(self):
        self.clickOnElement("xpath",self._gloabal_setting_xpath)

    def clickOnadminPersonalDashBoard(self):
        self.clickOnElement("xpath",self._persional_dasboard_xpath)

    def clickOnPowerPage(self):
        self.clickOnElement("xpath",self._power_page_xpath)

    def clickOnPowerMail(self):
        self.clickOnElement("xpath",self._power_mail_unlcok_xpath)

    def clickOnPowerLytics(self):
        self.clickOnElement("xpath",self._power_lytcis_unlock_xpath)