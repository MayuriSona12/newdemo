import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readproperties import Readconfig
from utilities.customeLogger import LogGen

class Test_001_Login:
    baseUrl= Readconfig.getAppUrl()
    username= Readconfig.getUsername
    password= Readconfig.getPassword()

    logger=LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("*******Test__01_Login**********")
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(10)
        act_title=self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.logger.info("*******Title test pass**********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshot\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*******Title test fail**********")
            assert False


    def test_login(self,setup):
        self.logger.info("*******Login with credential**********")
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(10)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.loginClick()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*******Login with credential test case pass**********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshot\\"+"test_login.png")
            self.driver.close()
            self.logger.error("*******Login with credential test case fail**********")
            assert False


