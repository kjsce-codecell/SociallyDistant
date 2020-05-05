import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/?hl=en')
        time.sleep(3)
        user = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
        user.clear()
        user.send_keys(self.username)
        time.sleep(0.3)
        passw = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
        passw.clear()
        passw.send_keys(self.password)
        time.sleep(1)
        log = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]').click()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        try:
            notNowButton = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
            time.sleep(1)
        except:
            print("No notification pop up")
            pass


    def visitLogin(self, tag):
        self.tag = tag
        search = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.clear()
        search.send_keys(self.tag)
        time.sleep(2)
        search.send_keys(Keys.ENTER)
        time.sleep(2)
        try:
            search.send_keys(Keys.ENTER)
            time.sleep(2)
        except:
            pass
        try:
            follow = self.driver.find_element_by_xpath(".//button[@class='_5f5mN       jIbKX  _6VtSN     yZn4P   ']")
            time.sleep(1)
            follow.click()
        except:
            print("Already Following")
            pass


    def likeComment(self, comment):
        driver = self.driver
        self.comment = comment
        post = driver.find_element_by_xpath("//div[@class='_9AhH0']")
        time.sleep(1)
        post.click()
        time.sleep(3)
        like = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button")
        time.sleep(1)
        like.click()
        time.sleep(3)
        comment = driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span._15y0l > button")
        time.sleep(1)
        comment.click()
        time.sleep(2)
        commentArea = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea")
        time.sleep(1)
        commentArea.send_keys(self.comment)
        time.sleep(3)
        postButton = driver.find_element_by_xpath(".//button[@class='sqdOP yWX7d    y3zKF     ']")
        postButton.click()


    def closeWithoutLogOut(self):
        self.driver.close()






if __name__ == "__main__":
    username = ''       #  provide an username or email id
    password = ''       #  provide the corresponding password    
    tag = 'kjsce_codecell'      #  provide the tag
    comment = 'Hey Thanks for the challenges'       #  provide a comment

    IB = Instagram(username, password)
    IB.login()
    IB.visitLogin(tag)
    IB.likeComment(comment)
    IB.closeWithoutLogOut()
    
