#!/usr/bin/env python
# coding: utf-8

# In[5]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd




print("veriler alınıyor lütfen bekleyiniz")
driver_path ="C:/Users/kullanıcı/Desktop/chromedriver.exe"
browser = webdriver.Chrome(driver_path)
browser.get("https://www.titck.gov.tr/kubkt")
browser.maximize_window()
time.sleep(3)



sayfa_sayisi = browser.find_element(By.XPATH, "//*[@id='posts_paginate']/span/a[6]").text
sayi = 1
liste = []
while sayi <= int(sayfa_sayisi):
    
    ilac_adlari = browser.find_elements(By.XPATH,"//*[@id='posts']/tbody/tr/td[1]")
    ilac_maddeleri = browser.find_elements(By.XPATH, "//*[@id='posts']/tbody/tr/td[2]")
    links = browser.find_elements(By.TAG_NAME, "a")
    kub = browser.find_elements(By.XPATH, "/html/body/div[5]/div/div/div/div/div/div/table/tbody/tr/td[6]/div/a")
    kt = browser.find_elements(By.XPATH, "/html/body/div[5]/div/div/div/div/div/div/table/tbody/tr/td[7]/div/a")
    for i in range(10):
        veri = { "ilaç adı": ilac_adlari[i].text,
                 "etken madde": ilac_maddeleri[i].text,
                 "kub": kub[i].get_attribute("href"),
                 "kt": kt[i].get_attribute("href")}
        liste.append(veri)
    browser.execute_script("window.scrollBy(0,-900)", "")
    konum = browser.find_element(By.XPATH, "//*[@id='posts_next']")
    konum.click()
    sayi = sayi +1
    time.sleep(3)
    
    

    
df = pd.DataFrame(liste)
df.to_excel("ilaç listesi.xlsx")
print("isleminiz bitti")

