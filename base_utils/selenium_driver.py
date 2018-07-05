from selenium import webdriver
from selenium.webdriver.common.by import By
from common_utils.custom_logger import customLogger
import logging
import os
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *




class SeleniumDriver():

    log=customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver=driver
        # self.driver=webdriver.Firefox()


    '''
    this function will take screen shot
    '''

    def takeScreenShot(self,resultMessage):

        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)
        self.driver.save_screenshot(destinationFile)
        self.log.info("Screenshot save to directory: " + destinationFile)


    # **************THIS FUNCTION IS TO GET THE ELEMENT TYPE**********
    # ################################################################
    def getByType(self,locatorType):

        locatorType=locatorType.lower()

        if locatorType=="id":
            return By.ID
        elif locatorType=="name":
            return By.NAME
        elif locatorType=="classname":
            return By.CLASS_NAME
        elif locatorType=="xpath":
            return By.XPATH
        elif locatorType=="cssselector":
            return By.CSS_SELECTOR
        elif locatorType=="linktext":
            return By.LINK_TEXT
        elif locatorType=="partiallinktext":
            return By.PARTIAL_LINK_TEXT
        elif locatorType=="tagname":
            return By.TAG_NAME
        else:
            self.log.info("Locator type " + locatorType +
                          " not correct/supported")
        return False

    # **************THIS FUNCTION IS TO GET THE ELEMENT**********
    # ################################################################

    def getElement(self,locatorType,locator):
        try:

            byType=self.getByType(locatorType)
            element=self.driver.find_element(byType,locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
            return element
        except Exception as e:
            self.log.info("Element  not found with locator: " + locator +
                          " and  locatorType: " + locatorType)

    def getElements(self,locatorType,locator):
        elements=None
        byType=self.getByType(locatorType)
        elements=self.driver.find_elements(byType,locator)
        self.log.info("Element found with locator: " + locator +
                      " and  locatorType: " + locatorType)
        return elements

    # ################################################################
    # **************THIS FUNCTION IS TO CLICK ON THE ELEMENT**********
    def clickOnElement(self,locatorType,locator):

        self.getElement(locatorType,locator).click()
        self.log.info("Clicked on element with locator: " + locator +
                      " locatorType: " + locatorType)

    # ###############################################################
    # **************THIS FUNCTION IS TO SEND DATA TO THE ELEMENT******

    def sendKeys(self,locatorType,locator,dataToBesend):
        self.getElement(locatorType,locator).send_keys(dataToBesend)
        self.log.info("Entered the data "+dataToBesend+" to the element "
                                                       "found by "+locator)
    # ################################################################
    # ***********************THIS FUNCTION IS TO GET TITLE*************

    def getTitle(self):
        return self.driver.title



    # ###################################################################
    '''
    verifying the title of the page
    '''
    def verifyPageTitle(self,title):
        actual_title=self.getTitle()
        self.log.info("The title of the page is "+actual_title)
        if actual_title==title:
            return True
        else:
            return False

    # #########################################################################

    '''
    this function is to check for the presence of element
    '''
    def isElementPresent(self,locatorType,locator):

        element=self.getElements(locatorType,locator)
        print("the total no of element is present is "+str(len(element)))
        if len(element) !=0:
            isPresent=True
            self.log.info("element on locator "+locator+" is present" )
        else:
            isPresent=False
            self.log.info("element on locator " + locator + " is not present")
        return isPresent

    # #########################################################################

    # **************Below functions are for the action function****************

    '''
    this function is for mouse hover 
    '''
    def mouseHoverOnElement(self,locatorType,locator):
        act=ActionChains(self.driver)
        element=self.getElement(locatorType,locator)
        act.move_to_element(element).perform()
        self.log.info("mouse hovered on the element found by locator "+locator )

    '''
    this function is to move to the cordinate of the element
    '''
    def moveToCordinateOfElement(self,locatorType,locator):
        act = ActionChains(self.driver)
        element = self.getElement(locatorType, locator)
        loc=element.location
        xcord=loc['x']
        ycord = loc['y']
        act.move_by_offset(xcord,ycord).perform()
        self.log.info("move to "+str(xcord)+"and "+str(ycord)+" of the element found by locator " + locator)

    '''
    This function to right click on the element
    '''

    def rightClickOnELement(self,locatorType,locator):
        act = ActionChains(self.driver)
        element = self.getElement(locatorType, locator)
        act.context_click(element).perform()
        self.log.info("right clicked on the element found by locator " + locator)

    '''
    This function is to open a link in another tab
    '''

    def openLinkOnAnotherTab(self,locatorType,locator):
        act = ActionChains(self.driver)
        self.rightClickOnELement(locatorType,locator)
        act.send_keys(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        self.log.info("opened the link on another tab, found by locator " + locator)

    '''
    This function will open an empty tab
    '''
    def openNewTab(self,url):
        script="window.open('{0}','new window')"
        actualScript=script.format(url)
        self.driver.execute_script(actualScript)



    # ############################################################################
    # *************Below functions are for select functions***********************

    '''
    This function is to select element by text
    '''

    def selectByText(self,locatorType,locator,textToSelect):
        element=self.getElement(locatorType,locator)
        sel=Select(element)
        sel.select_by_visible_text(textToSelect)
        self.log.info("select the element on text " + textToSelect)

    '''
    This function is to select element by value
    '''

    def selectByValue(self,locatorType,locator,valueToSelect):
        element=self.getElement(locatorType,locator)
        sel=Select(element)
        sel.select_by_value(valueToSelect)
        self.log.info("select the element on value " + valueToSelect)

    '''
       This function is to select element by index
    '''

    def selectByIndex(self, locatorType, locator, indexToSelect):
        element = self.getElement(locatorType, locator)
        sel = Select(element)
        sel.select_by_index(indexToSelect)
        self.log.info("select the element on index " + indexToSelect)

    '''
    This function is to verify element in the dropdown
    '''

    def verifyElementInDropDown(self,locatorType,locator,textToVerify):
        element = self.getElement(locatorType, locator)
        sel = Select(element)
        isPresnt=False
        allElements=sel.options
        for elements in range (0,len(allElements)):
            if allElements[elements].text ==textToVerify:
                isPresnt=True
                print(textToVerify+ " is present in the drop down")
                self.log.info("found the element "+allElements[elements].text+" in the dropdown box")
                break
            else:
                continue
        return isPresnt
    # ###########################################################################

    # **************below functions are to handel window ***********************

    '''
    this function is to handel window by its no
    
    '''
    def handelWindowByNo(self,windowNo):
        allIds=self.driver.window_handles
        self.log.info("the total no of window is "+str(len(allIds)))
        print("the total no of window is "+str(len(allIds)))
        for id in range(0,len(allIds)):
            if id==windowNo-1:
                self.driver.switch_to.window(allIds[id])
                self.log.info("switched to the desired window")
    '''
    This function is to handel window by its title
    '''

    def handelWindowByTitle(self,windowTitle):

        pid=self.driver.current_window_handle
        ids=self.driver.window_handles

        for id in ids:
            if pid!=id:
                self.driver.switch_to.window(id)
                actualTitle=self.driver.title
                if actualTitle==windowTitle:
                    self.driver.switch_to.window(id)
                    self.log.info("switched to the desired window")
                    break
                else:
                    continue
    # ##############################################################################
    # ********************below functions are to handel the alert*******************

    '''
    this function is to handel the alert 
    '''
    def handelAlert(self,okOrCancel):

        if okOrCancel.lower()=="ok":
            alt=self.driver.switch_to.alert
            alt.accept()
            self.log.info("alert is accepted")
        elif okOrCancel.lower()=="cancel":
            alt=self.driver.switch_to.alert
            alt.dismiss()
            self.log.info("alert is dismissed")

    '''
    this function is to read the text from alert
    '''

    def getAlertText(self):
        alt=self.driver.switch_to.alert
        return alt.text

    # ###########################################################################
    # ********** below functions are to scroll **********************************
    '''
    This function is to scroll up or down
    '''
    def scroll(self,upOrDown):

        if upOrDown.lower()=="up":
            self.driver.execute_script("scroll(0, -1500);")
        elif upOrDown.lower()=="down":
            self.driver.execute_script("scroll(0, 1500);")

    '''
    This function is to scroll to exact element
    '''

    def scrollToElement(self,locatorType,locator):

        element=self.getElement(locatorType,locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);",element)

    # ##############################################################################
    # *************Below function is for webdriver wait*****************************

    '''
    This is for the visible of the element
    '''
    def waitForTheVisibilty(self,timeInSec,locatorType,locator):
        wait=WebDriverWait(self.driver,timeInSec,poll_frequency=1,
                           ignored_exceptions=(NoSuchElementException,ElementNotInteractableException,ElementNotVisibleException))

        wait.until(expected_conditions.visibility_of(self.getElement(locatorType,locator)))

    '''
    This is to wait for the element to click
    '''

    def waitForTheClickable(self,timeInSec,locatorType,locator):
        wait = WebDriverWait(self.driver, timeInSec, poll_frequency=1,
        ignored_exceptions = (NoSuchElementException, ElementNotInteractableException, ElementNotVisibleException))
        wait.until(expected_conditions.element_to_be_clickable(self.getByType(locatorType),locator))

    '''
    This is to wait for the element to be present
    '''

    def waitForThePrsenceOfElement(self,timeInSec,locatorType,locator):
        wait = WebDriverWait(self.driver, timeInSec, poll_frequency=1,
                             ignored_exceptions=(
                             NoSuchElementException, ElementNotInteractableException, ElementNotVisibleException))
        wait.until(expected_conditions.presence_of_element_located(self.getByType(locatorType),locator))

    def waitforTilteOfThePage(self,timeInSec,title):
        wait=WebDriverWait(self.driver,timeInSec,poll_frequency=1,
                           ignored_exceptions=(
                           NoSuchElementException, ElementNotInteractableException, ElementNotVisibleException))
        wait.until(expected_conditions.title_contains(title))

    # will add more wait