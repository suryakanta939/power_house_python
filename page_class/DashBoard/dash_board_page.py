from base_utils.selenium_driver import SeleniumDriver

class DashBoard(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)

    _dash_board_xpath="//a[text()='Dashboards']"
    _home_page_xpath="//a[text()='Home Page']"
    _admin_dash_board_xpath="//a[text()='Admin Dashboard']"
    _personal_dash_board_xpath="//a[text()='Personal Dashboard']"

    def mouseHoveOnDashBoard(self):
        self.moveToCordinateOfElement("xpath",self._dash_board_xpath)
        self.mouseHoverOnElement("xpath",self._dash_board_xpath)

    def clickOnHomePage(self):
        self.waitForTheVisibilty(10,"xpath",self._home_page_xpath)
        self.clickOnElement("xpath",self._home_page_xpath)

    def clickOnAdminDashBoard(self):
        self.waitForTheVisibilty(10, "xpath", self._admin_dash_board_xpath)
        self.clickOnElement("xpath", self._admin_dash_board_xpath)

    def clickOnPersonalDashBoard(self):
        self.waitForTheVisibilty(10, "xpath", self._personal_dash_board_xpath)
        self.clickOnElement("xpath", self._personal_dash_board_xpath)

