from selenium import webdriver
import os
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class InvokeBrowser():

    def openBrowser(self,browserName):

        driver=None
        if browserName.lower()=="chrome":
            currentDir=os.path.dirname(__file__)
            destinationDir="../all_drivers/"
            destinationFile=destinationDir+"chromedriver.exe"
            target=os.path.join(currentDir,destinationFile)
            driver=webdriver.Chrome(target)
            driver.get("https://app.pohostaging.com/login/")
            driver.maximize_window()

        elif browserName.lower()=="firefox":
            binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
            driver = webdriver.Firefox(firefox_binary=binary)
            driver.get("https://app.pohostaging.com/login/")
            driver.maximize_window()

        return driver
