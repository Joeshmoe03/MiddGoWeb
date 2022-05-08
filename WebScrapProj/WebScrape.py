#These are all of our project dependencies so far
from bs4 import BeautifulSoup
from lockfile import Error
import pandas
import json
import requests
import urllib.request

class Scrapify():
    def __init__(self, link, output = None):
        self.link = link
        self.r = requests.get(self.link)
        self.webUrl = urllib.request.urlopen(self.link)
        self.output = output
        self.readHTML()

    def makeTXT(self):
        with open("scrapedata.txt", "w") as self.filewritten:
            self.filewritten.write(self.r.text)

    def readHTMLrequestSuccess(self):
        return self.webUrl.getcode()

    def readHTML(self):
        try:
            assert(self.readHTMLrequestSuccess() == 200) # revise to see if correctly handles request validation
            self.data = self.webUrl.read()
        except:
            assert ConnectionError

    def parseAllHTML(self, attr):
        parsedHTML = BeautifulSoup(self.data, "html5lib")
        self.output = parsedHTML.findAll(str(attr))[13:14] #delete the 13:14 this is just for testing
        return Scrapify(self.link, self.output)

    def parseHTML(self, attr):
        parsedHTML = BeautifulSoup(self.data, "html5lib")
        output = parsedHTML.find(str(attr))
        return Scrapify(self.link, output)

    def __str__(self):
        return str(self.output)
 

HTMLfile = Scrapify("http://go.middlebury.edu/gotionary.php")
TXTpage = HTMLfile.makeTXT()
output = HTMLfile.parseHTML('p')
print(output)
print(output.parseHTML('b'))
