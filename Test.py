from selenium import webdriver
import time
import urllib.request
import os
from selenium.webdriver.common.keys import Keys





chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-startup-window")

browser = webdriver.Chrome('C:/Users/Pranav Sandeep/Downloads/chromedriver_win32/chromedriver.exe', chrome_options=chrome_options)

browser.get("https://www.google.com/")



class Test():
    def __init__(self):
        pass

    def Download_Images(self, key_word):


        search = browser.find_element_by_name('q')



        search.send_keys(key_word,Keys.ENTER)

        elem = browser.find_element_by_link_text('Images')
        elem.get_attribute('href')
        elem.click()

        value = 0
        for i in range(20):
           browser.execute_script("scrollBy('+ str(value) +',+1000);")
           value += 1000
           time.sleep(3)

        elem1 = browser.find_element_by_id('islmp')

        sub = elem1.find_elements_by_tag_name("img")

        try:
            os.mkdir('downloads')
        except FileExistsError:
            pass

        count = 0
        Limit = int(input("Whats the maximum files do u want"))

        Limit += 1

        flag = 1

        for i in sub:

            if flag >= Limit:
                break
            src = i.get_attribute('src')
            try:
                if src != None:
                    src  = str(src)
                    print(src)
                    count+=1
                    urllib.request.urlretrieve(src, os.path.join('downloads','image'+str(count)+'.jpg'))
                else:
                    raise TypeError
            except TypeError:
                print('fail')

            flag += 1




InternyetImageSearcher = Test()

InternyetImageSearcher.Download_Images("Rick Astely")