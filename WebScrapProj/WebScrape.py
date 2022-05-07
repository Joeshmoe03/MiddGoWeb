from bs4 import BeautifulSoup
import pandas

#These are all of our project dependencies so far
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
        self.links = []

    def formatPage(self, parser):
        self.content = self.driver.page_source
        self.soup = BeautifulSoup(self.content, str(parser))

    def searchHyperlink(self):
        for i, link in enumerate(self.soup.findAll("a")):
            self.links.append(dict(i, link.get("href")))
        return self.links
    


#textelems = driver.
    def close(self):
        self.driver.quit()

page = Scrapify("http://go.middlebury.edu/gotionary.php")
page.formatPage("html5lib")
print(page.searchHyperlink()[0:100])