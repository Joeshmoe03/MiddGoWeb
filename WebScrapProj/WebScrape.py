#These are all of our project dependencies so far
from bs4 import BeautifulSoup
import pandas
import json
import requests
import urllib.request

class Scrapify():
    def __init__(self, link):
        self.link = link
        self.r = requests.get(self.link)
        self.webUrl = urllib.request.urlopen(self.link)

    def makeTXT(self):
        with open("scrapedata.txt", "w") as self.filewritten:
            self.filewritten.write(self.r.text)

    def readHTMLrequestSuccess(self):
        return self.webUrl.getcode()

    def readHTML(self):
        try:
            self.readHTMLrequestSuccess()
            self.data = self.webUrl.read()
        except:
            assert ConnectionError

    def parseHTML(self, *attrs):
        self.parsedHTML = BeautifulSoup(self.data, "html5lib")
        self.parsedHTML

HTMLfile = Scrapify("http://go.middlebury.edu/gotionary.php")
TXTpage = HTMLfile.makeTXT()
HTMLfile.readHTML()
HTMLfile.parseHTML()


