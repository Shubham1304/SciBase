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
print("Enter the name of the author you want to search:")
search=input()
url="https://scholar.google.co.in/citations?view_op=search_authors&mauthors=" + search

browser = webdriver.Firefox()
browser.get(url)
elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gsc_sa_ccl"]/div/div/h3/a/span')))
source = browser.page_source
button = browser.find_element_by_css_selector('#gsc_sa_ccl > div > div > h3 > a > span')
button.click()
element = WebDriverWait(browser,30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#gsc_a_b > tr:nth-child(1) > td.gsc_a_t > a')))
source1=browser.page_source
soup = BeautifulSoup(source1,'html.parser')
raw_name = soup.find("td",{"class":"gsc_a_t"})
name=raw_name.find("a",{"class":"gsc_a_at"})
#print(name.text)
str1=[]
str1.append("{\""+name.text+"\":{")


button2 = browser.find_element_by_css_selector('tr.gsc_a_tr:nth-child(1) > td:nth-child(2) > a:nth-child(1)')
button2.click()
source2=browser.page_source
soup = BeautifulSoup(source2,'html.parser')
# Path to be created
path = "/home/shubham/directory1"
os.makedirs(path, exist_ok=True)
print ("Path is created")
file=open('/home/shubham/directory1/abcd.json',"a")
for i in range(3,5):
    s1='#gs_n > center:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child('
    s3=') > a:nth-child(1)'
    #s2=str(i)
    button3=browser.find_element_by_css_selector(s1+str(i)+s3)
    button3.click()                             #gs_n > center:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(4) > a:nth-child(1)
    source3=browser.page_source                 #gs_n > center:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(5) > a:nth-child(1)
    soup=BeautifulSoup(source3,'html.parser')
#str2=[]
#ele=[]
#for i in range(0,5):
    for ele in soup.find_all("div",{"class":"gs_ri"}):  #for the whole class
        for ele1 in ele.find_all("h3",{'class':"gs_rt"}):  #for the name of paper
            for a1 in ele1.find_all('a'):
                redditAll1 = ele1.find_all("a")
                print(len(redditAll1))
                leng1=len(redditAll1)
                str1.append("\""+a1.text+"\":[{")
                leng1-=1
        for ele2 in ele.find_all("div",{'class':'gs_a'}):   #for the names of autors
            for a2 in ele2.find_all('a'):
                redditAll2 = ele2.find_all("a")
                print(len(redditAll2))
                leng2=len(redditAll2)
                str1.append("\"Author\":\"" + a2.text + "\"}")
                leng2-=1
                if leng2 != 0:
                    str1.append(",")
                else:
                    str1.append("]")
                    if leng1 !=0:
                        str1.append(",")

    str1.append("}}")
    var = ' '.join(str1)
    file.write(var)
file.close()
