#!/usr/local/bin/python 

from selenium import webdriver
#from page_objects.inbox import inbox
import time

class signIn():

    def sign_in(self, signin_id, password):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://accounts.google.com/signin')
        self.driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(signin_id)
        self.driver.find_element_by_id('identifierNext').click()
        time.sleep(5)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_id('passwordNext').click()
        
        self.driver.find_element_by_class_name('class="T-I J-J5-Ji T-I-KE L3"')
        self.driver.find_element_by_class_name('aio UKr6le')
        self.driver.find_element_by_class_name('aAy aIf-aLe J-KU-KO')
        self.driver.find_element_by_class_name('aAy aKe-aLe J-KU-KO')
        self.driver.find_element_by_class_name('aAy aJi-aLe J-KU-KO')
        self.driver.find_element_by_class_name('aKw')
        self.driver.find_element_by_class_name('gb_0 gb_If gb_Pf gb_pe gb_jb')
        self.driver.find_element_by_class_name('gb_Ne')
        self.driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[1]/div[1]/svg/path')






        return inbox(self.driver)

