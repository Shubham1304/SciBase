import os , sys
from selenium  import webdriver
from selenium.webdriver.common.keys import Keys
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import errno
search="vapnik"
url="https://scholar.google.co.in/scholar?oi=bibs&hl=en&cites=8608559880368280977,257377035427477106,13538606778381662047,7584568690943495592,13074838339646797994"
browser = webdriver.Firefox()
browser.get(url)
source=browser.page_source
soup=BeautifulSoup(source,'html.parser')
str=[]
str.append('{\"vapnik\":{')
str1=[]
str2=[]
ele=[]
#for i in range(0,5):
for ele in soup.find_all("div",{"class":"gs_ri"}):  #for the whole class
    for ele1 in ele.find_all("h3",{'class':"gs_rt"}):
        for a1 in ele1.find_all('a'):
            str1.append(a1.text)
    for ele2 in ele.find_all("div",{'class':'gs_a'}):
        for a2 in ele2.find_all('a'):
            str1.append(a2.text)

    #str1.append(ele1.text)
    #print (ele1.text)
    #containing the name of paper and citing authors
    #for ele1 in ele.find("h3",{"class":"gs_rt"}): #for the name of paper
    #    for a1 in ele1.find_all('a'):
    #        str1.append(a1.text)
#for i in range (0,5):
print(str1)
#print(str2)
        #    str.append('\"'+a1.text+'\":[')
        #    for ele2 in soup.find_all("div",{"class":"gs_a"}): #for citing authors name
        #        for a2 in ele2.find_all('a'):
        #                str.append('"'+a2.text+'",')
        #str.append('],')
str.append('}}')
var = ' '.join(str)

#print(str)
#for i in range(0,5):
    #authorsname()
    #str.append('}}')
    #var = ' '.join(str)
    #print (str)
#{"mainauthorname_vapnik":{"papername1":["citingauthor1","cauthor2","cauthor3"],"papername2":["cauthor1","cauthor2"]}}
