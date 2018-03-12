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
import time

def file_open():
    path = "/home/shubham/directory1"
    os.makedirs(path, exist_ok=True)
    print ("Path is created")
    file=open('/home/shubham/directory1/abcd1.json',"a")


def scraper(soup,str1):
    i=1
    browser = webdriver.Firefox()
    for i in range(1,3):
        s1='#gs_n > center:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child('
        s3=') > a:nth-child(1)'
        #s2=str(i)
        if i!=1:
            button3=browser.find_element_by_css_selector(s1+str(i+1)+s3)
            button3.click()
            url3=browser.current_url
            browser.quit()
            browser = webdriver.Firefox()
            browser.get(url3)                          #gs_n > center:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(4) > a:nth-child(1)
            source3=browser.page_source                 #gs_n > center:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(5) > a:nth-child(1)
            soup=BeautifulSoup(source3,'html.parser')
        url=browser.current_url
    #str2=[]
    #ele=[]
    #for i in range(0,5):
        j=1;
        for ele in soup.find_all("div",{"class":"gs_ri"}):  #for the whole class
            #print("This is the main loop")
            for ele1 in ele.find_all("h3",{'class':"gs_rt"}):  #for the name of paper
                #print("Hello loop 1 I am searching for papers name")
                for a1 in ele1.find_all('a'):
                    '''redditAll1 = ele1.find_all("a")
                    print(len(redditAll1))
                    leng1=len(redditAll1)'''
                    #str1.append("\""+a1.text+"\":[")
                    str1.append("paper:" + a1.text+",")
                    print(str1)
                    time.sleep(5)
                    #print("Hello loop 2 I am searching for papers name")
                    #leng1-=1
            for ele2 in ele.find_all("div",{'class':'gs_a'}):   #for the names of autors
                i=1
                #print("Hello First loop of papers name")
                for a2 in ele2.find_all('a'):
                    #print("Hello second loop of papers name ")
                    #str1.append("{\"Author\":\"" + a2.text + "\",")
                    str1.append("author:"+a2.text+",")
                    print(str1)
                    s4='/html/body/div/div[11]/div[2]/div[2]/div[2]/div['
                    s5=str(j)
                    s6=']/div[2]/div[1]/a['
                    s7=str(i)
                    s8=']'
                    time.sleep(2)
                    button4=browser.find_element_by_xpath(s4+s5+s6+s7+s8)
                    button4.click()
                    elem2 = WebDriverWait(browser,100).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[14]/div[2]/div/div[2]/div/div[2]/div[2]')))
                    source4=browser.page_source
                    soup2=BeautifulSoup(source4,'html.parser')
                    inst_data=soup2.find("div",{"class":"gsc_prf_il"})
                    inst_text=inst_data.text
                    i+=1
                    str1.append("\"Institute\":\""+inst_text+"\"},")
                    print(str1)
                    browser.get(url)
                    elem3 = WebDriverWait(browser,1000).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[11]/div[2]/div[2]/div[3]/div[1]/center/table/tbody/tr/td[1]/span')))
                    time.sleep(2)
                    '''redditAll2 = ele2.find_all("a")
                    print(len(redditAll2))
                    leng2=len(redditAll2)
                    str1.append("{\"Author\":\"" + a2.text + "\"}")
                    leng2-=1
                    if leng2 != 0:
                        str1.append(",")
                    else:
                        str1.append("]")
                        if leng1 !=0:
                            str1.append(",")'''
            j+=1
            browser.get(url)
    var = ' '.join(str1)
    print(str1)
    print(var)
    file.write(var)
    file.close()
    return

def main():

    file_open()
    print("Enter the name of the author you want to search:")
    search=input()
    url="https://scholar.google.co.in/citations?view_op=search_authors&mauthors=" + search
    browser = webdriver.Firefox()
    browser.get(url)
    elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gsc_sa_ccl"]/div/div/h3/a/span')))
    source = browser.page_source
    time.sleep(5)
    button = browser.find_element_by_css_selector('#gsc_sa_ccl > div > div > h3 > a > span')
    button.click()
    url1=browser.current_url
    browser.quit()
    browser = webdriver.Firefox()
    browser.get(url1)
    element = WebDriverWait(browser,30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#gsc_a_b > tr:nth-child(1) > td.gsc_a_t > a')))
    source1=browser.page_source
    soup = BeautifulSoup(source1,'html.parser')
    raw_name = soup.find("td",{"class":"gsc_a_t"})
    name=raw_name.find("a",{"class":"gsc_a_at"})
    #print(name.text)
    str1=[]
    #str1.append("{\""+name.text+"\":{")
    str1.append(name.text+";")
    print(str1)
    time.sleep(5)
    button2 = browser.find_element_by_css_selector('tr.gsc_a_tr:nth-child(1) > td:nth-child(2) > a:nth-child(1)')
    button2.click()
    url2=browser.current_url
    browser.quit()
    browser = webdriver.Firefox()
    browser.get(url2)
    source2=browser.page_source
    soup = BeautifulSoup(source2,'html.parser')
    scraper(soup,str1)
    return


main()
