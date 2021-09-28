# $$$$$$$$$$$$$$$$$$$$$$$$

from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from random import seed
from random import random
from time import process_time, sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from creatingcsv import csv_making
import csv

'''
from selenium.webdriver.chrome.service import Service
service = Service('C:/Users/Seb/PycharmProjects/pythonProjectTinBo/chromedriver_win32 (1)/chromedriver.exe')
service.start()
'''


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument('headless')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('???')
chrome_options.add_argument('--no-proxy-server')

driver = webdriver.Chrome(ChromeDriverManager().install())


# driver = webdriver.Chrome('/home/odg/shubham/scraping/chromedriver',chrome_options=chrome_options)

#list all industry

# header = ['Name', 'Last_Name', 'Job_Title', 'Profile_Url']

# with open('domain.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)


driver.get('https://www.vegasinsider.com/mlb/scoreboard/scores.cfm/game_date/09-22-2021')
driver.maximize_window()
time.sleep(5)
# driver.find_element_by_xpath('/html/body/div[2]/div[10]/div[7]/a').click()
res=driver.page_source
soup=BeautifulSoup(res,'html.parser')
  





##################################################################################
data=[]
data_list=[]
new=[]

# table_header=find_all


def filter(data_list):
    for i in data_list:
            # print(i)
            if "\xa0\n\n" in i:
                # if ""
                    new.append(i.replace('\xa0\n\n',' ').strip())
            else:
                    new.append(i.strip()) 
    try:
        new[1]=new[1].replace('«','').strip()
    except:
        pass                      
    for i in new:
        if 'Teams' in i:
            new[1]="     "+i+"           "
        else:
            pass   

    data_list.clear()                
    return new


single_table=soup.find_all('td',{'class':'sportPicksBorder'})
for s in single_table:
    sportPicksBg=s.find_all('tr',{'class','sportPicksBg'})
    table=s.find_all('tr',{'class':'tanBg'})

    for bg in  (sportPicksBg):
        # print([t.text])
        bg_content=bg.find_all('td')
        for d in bg_content:
            data_list.append(d.text.strip())
        # filter(data_list)    
        csv_making(filter(data_list))    
        for t in table:
            content=t.find_all('td')
            for c in content:
                data_list.append(c.text.strip())
            csv_making(filter(data_list))    

        # print(data_list)    
   