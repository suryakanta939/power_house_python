from page_class.Power_house_service_page.power_house_service_page import PowerHouseServices
from time import sleep

class PowerSitePage(PowerHouseServices):

    def __init__(self,driver):
        super().__init__(driver)


    _free_trial_xpath="//a[@href='/subscriptions/?add-to-cart=143']"
    _launching_plan_xpath="//a[@href='/subscriptions/?add-to-cart=145']"
    _thriving_plan_xpath="//a[@href='/subscriptions/?add-to-cart=146']"
    _scaling_plan_xpath="//a[@href='/subscriptions/?add-to-cart=147']"
    _view_cart_xpath="//a[text()='View cart']"

    def clickOnFreeTrialXpath(self):
        self.mouseOverOnPowerhouseService()
        sleep(1)
        self.clickOnPowerSite()
        self.clickOnElement("xpath",self._free_trial_xpath)

    def clickOnLaunchingXpath(self):
        self.mouseOverOnPowerhouseService()
        sleep(1)
        self.clickOnPowerSite()
        self.clickOnElement("xpath",self._launching_plan_xpath)

    def clickOnthrivingPlan(self):
        self.mouseOverOnPowerhouseService()
        sleep(1)
        self.clickOnPowerSite()
        self.clickOnElement("xpath",self._thriving_plan_xpath)

    def clcikOnScalingPlan(self):
        self.mouseOverOnPowerhouseService()
        sleep(1)
        self.clickOnPowerSite()
        self.clickOnElement("xpath",self._scaling_plan_xpath)

    def clickOnViewCart(self):
        self.waitForTheVisibilty(10,"xpath",self._view_cart_xpath)
        self.clickOnElement("xpath",self._view_cart_xpath)

