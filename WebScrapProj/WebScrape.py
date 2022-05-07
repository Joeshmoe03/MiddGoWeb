#These are all of our project dependencies so far
from bs4 import BeautifulSoup
import pandas
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Scrapify():
    def __init__(self, link):
        #This block of code oppens a chrome browser in a hidden format, and then gets the specified website
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("headless")
        self.options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.link = link
        self.driver.get(self.link)
        self.templist = []

    def formatPage(self, parser):
        self.content = self.driver.page_source
        self.soup = BeautifulSoup(self.content, str(parser))

    def filter


    def close(self):
        self.driver.quit()

page = Scrapify("http://go.middlebury.edu/gotionary.php")
page.formatPage("html5lib")
print(page)
