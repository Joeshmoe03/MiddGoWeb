from bs4 import BeautifulSoup
import pandas

#These are all of our project dependencies so far
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Scraper:
    def __init__(self,
                link):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("headless") 
        self.options.add_argument("start-maximized")
        self.link = link
        self.results = []
        
    def OpenPage(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.driver.get(str(self.link))
        self.content = self.driver.page_source
        self.soup = BeautifulSoup(self.content, features="html5lib")

    def SearchParameters(self, name = None, attr = None):
        self.results.append(self.soup.findAll(name, attr))

    def Output(self):
        return self.results[0:10]

    def ClosePage(self):
        self.driver.quit()

mainweb = Scraper("http://go.middlebury.edu/gotionary.php")
mainweb.OpenPage()
mainweb.SearchParameters("a")
mainweb.ClosePage()
print(mainweb.Output())