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


class FeedbackForm:
    def __init__(self, link):
        self.browser = webdriver.Chrome()
        browser = self.browser
        browser.get(link)
        time.sleep(5)

    def fill(self, answers):
        self.ans = answers
        browser = self.browser
        i = 0
        j = 0
        k=0
        other = browser.find_elements_by_xpath(".//input[@class='quantumWizTextinputSimpleinputInput exportInput']")
        # print(len(other))
        input_elements = []
        input_elements = browser.find_elements_by_xpath(".//input[@class='quantumWizTextinputPaperinputInput exportInput']")
        # print(len(input_elements))   #6
        for item in browser.find_elements_by_class_name('freebirdFormviewerViewNumberedItemContainer'):
            if(i == 1 or i == 2 or i == 4 or i == 5 or i == 6):     #  cases where we need to select an option
                if(self.ans[i+k] == 5 and i == 1 or self.ans[i+k] == 6 and i == 2):     #  other corner case taken care here
                    xpath = '//*[@id="mG61Hd"]/div/div/div[2]/div[%d]/div/div[2]/div/span/div/div[%d]/div/label/div/div[1]/div/div[3]/div'%(i+1,self.ans[i+k])
                    #  here if we wanted to randomize the output or selection we could use random from 1-5/6 instead of choosing the div of ans
                    if(self.ans[i+k] == 5 and i == 1):
                        z = 0
                    else:
                        z=1
                    other[z].clear()
                    other[z].send_keys(self.ans[i+k+1])
                    k += 1
                    print(k)
                else:
                    xpath = '//*[@id="mG61Hd"]/div/div/div[2]/div[%d]/div/div[2]/div/span/div/div[%d]/label/div/div[1]/div/div[3]/div'%(i+1,self.ans[i+k])
                
                item_to_click = browser.find_element_by_xpath(xpath)    
                item_to_click.click()              
                time.sleep(0.5)
                
            else:
                time.sleep(0.5)
                input_elements[j].clear()
                input_elements[j].send_keys(self.ans[i+k])
                time.sleep(0.5)
                j += 1

            i += 1
            print(i+k)

    def send(self):
        send_key = self.browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div/span/span')
        send_key.click()

    def close(self):
        self.browser.close()
        print("Success!!")


if __name__ == "__main__":

    link ='https://docs.google.com/forms/d/e/1FAIpQLSc_22gDAQHTHHv5dAP206n32jyTxHMzsGtULSH-GkdQ9Mk5qg/viewform'
    answers = ('Zalak Bhojani', 2, 1, 'zalak.b@somaiya.edu', 2, 2, 2, 'The initiative is well balanced especially considering it is lockdown period. Maybe increase the interaction on the discord server', 'NONE', 'Yes', 'NONE')
    # fill in the answers to submit  

    fb=FeedbackForm(link)
    fb.fill(answers)
    fb.send()
    # fb.close()
