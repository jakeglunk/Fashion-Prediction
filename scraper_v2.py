import requests
from bs4 import BeautifulSoup
import urllib.request
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options

import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

list=[]


def scraper(url):
    source_code = requests.get(url)

    plain_text = source_code.text

    global page_source

    soup = BeautifulSoup(page_source,features="html.parser")

    print("Getting Links...")

    x=0
    y=0

    while x<100:
        x=x+1
        y=x*2200
        for link in soup.find_all("img",{"class":"hCL kVc L4E MIw"}):
            href = link.get('srcset')
            href = str(href)
            href = href.split(" ")


            href = href[0]

            print(href)

            list.append(href)

        browser.execute_script("window.scrollTo(0, {})".format(y))

        page_source = browser.page_source
        soup = BeautifulSoup(page_source,features="html.parser")

        time.sleep(0.5)

    print("Saving Images...")

    print(list)

    for item in list:
        try:
            list.remove("None")
        except ValueError:
            pass

    print(list)

    alist = list_cleaner(list)

    print(alist)

    x=521
    for item in alist:

        img_name = x

        full_name = str(img_name) + ".jpg"

        urllib.request.urlretrieve(item, full_name)

        x=x+1

    print("Done")

def login(login, pw, download=True):
        download = download
        # self.browser = webdriver.Firefox()
        global browser
        browser = webdriver.Chrome(executable_path='C:/Users/Jake/Downloads/chromedriver_win32/chromedriver.exe',options=chrome_options)

        browser.get("https://www.pinterest.com/search/pins/?rs=ac&len=2&q=mens%20fashion&eq=mens%20fas&etslf=5070&term_meta[]=mens%7Cautocomplete%7C0&term_meta[]=fashion%7Cautocomplete%7C0")
        time.sleep(1)
        logbutton = browser.find_element_by_xpath('//*[@id="HeaderContent"]/div/div[1]/div/div/div[2]/button')
        logbutton.click()
        time.sleep(1)
        email_elem = browser.find_element_by_name('id')
        email_elem.send_keys(login)
        time.sleep(1)
        password_elem = browser.find_element_by_name('password')
        password_elem.send_keys(pw)
        time.sleep(1)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(2)

        global page_source
        page_source= browser.page_source

def list_cleaner(list):
    final =[]
    george = set(list)
    for item in george:
        final.append(item)

    try:
        final.remove("None")
    except ValueError:
        pass

    return final


login("jakeglunk0@gmail.com","Chuckeyt7")
scraper("https://www.pinterest.com/search/pins/?rs=ac&len=2&q=mens%20fashion&eq=mens%20fas&etslf=5070&term_meta[]=mens%7Cautocomplete%7C0&term_meta[]=fashion%7Cautocomplete%7C0")
browser.close()
