#These are all of our project dependencies so far
from bs4 import BeautifulSoup
import pandas
import json
import requests

class Scrapify():
    def __init__(self, link):
        self.link = link
        self.r = requests.get(self.link)

    def makeTXT(self):
        with open("scrapedata.txt", "w") as file:
            file.write(self.r.text)
        return file
    

HTMLfile = Scrapify("http://go.middlebury.edu/gotionary.php")
TXTpage = HTMLfile.makeTXT()



