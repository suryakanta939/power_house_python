from base_utils.selenium_driver import SeleniumDriver

class PowerHouseServices(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)

    _powerhouse_service_xpath="//a[text()='PowerHouse Services']"
    _power_pages_xpath="//a[text()='PowerPages']"
    _power_site_xpath = "//a[text()='PowerSites']"
    _power_mail_xpath="//a[text()='PowerMail']"
    _power_lytics_xpath="//a[text()='PowerLytics']"
    _power_lunch_xpath="//a[text()='PowerLaunch']"

    def mouseOverOnPowerhouseService(self):
        self.moveToCordinateOfElement("xpath",self._powerhouse_service_xpath)
        self.mouseHoverOnElement("xpath",self._powerhouse_service_xpath)

    def clickOnPowerSite(self):
        self.waitForTheVisibilty(10,"xpath",self._power_site_xpath)
        self.clickOnElement("xpath",self._power_site_xpath)

    def clickOnPowerPage(self):
        self.waitForTheVisibilty(10, "xpath",self._power_pages_xpath)
        self.clickOnElement("xpath",self._power_pages_xpath)

    def clickOnPowerMail(self):
        self.waitForTheVisibilty(10,"xpath",self._power_mail_xpath)
        self.clickOnElement("xpath",self._power_mail_xpath)

    def clickOnPowerLytics(self):
        self.waitForTheVisibilty(10, "xpath",self._power_lytics_xpath)
        self.clickOnElement("xpath",self._power_lytics_xpath)

    def clickOnPowerLunch(self):
        self.waitForTheVisibilty(10, "xpath",self._power_lunch_xpath)
        self.clickOnElement("xpath",self._power_lunch_xpath)
