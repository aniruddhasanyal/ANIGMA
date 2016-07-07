# from six.moves.urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


def getwebtxt(url='https://en.wikipedia.org/wiki/Machine_learning'):
    f = urlopen(url)
    myfile = f.read()
    soup = BeautifulSoup(myfile, 'html.parser')
    text = re.sub(r'[0-9]|[+=\'\"<>{}()]', '', soup.get_text())
    return text
