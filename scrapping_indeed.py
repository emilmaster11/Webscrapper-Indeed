from re import A
import pandas as pd
from cgitb import enable
from turtle import position
from tkinter.tix import Select
from selenium import webdriver
from lib2to3.pgen2 import driver
import undetected_chromedriver as uc
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains ## MAYBE
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException


def get_url(position, location):
    
    """Generate url from position and location"""
    template = 'https://www.indeed.de/jobs?q={}&l={}'
    position = position.replace(' ', '+')
    location = location.replace(' ', '+')
    url = template.format(position, location)
    
    return url



def scrapping(url):

 driver = webdriver.Chrome(executable_path=r'PATH TO CHROMERDRIVER.EXE')
 dic = {'Titel':[],'Name':[],'Zusammenfassung':[]}
 
 ###Wie viele Seiten er Scrappen soll###
 for x in range(10):

    basic_url = url + str('&start=') #https://www.indeed.de/jobs?q={}&l={}&start=

    basic_url_seiten =basic_url +str(x*10) # #https://www.indeed.de/jobs?q={}&l={}&start=0
    
    try:
     driver.get(basic_url_seiten)

    except:
     break 

    try:
     job_titel = driver.find_elements(by=By.CLASS_NAME, value="jobTitle")
     name_unternehmen = driver.find_elements(by=By.CLASS_NAME,value="companyName")
     zusammenfassung = driver.find_elements(by=By.CLASS_NAME, value="job-snippet")

    except:
     break

    int = 0
    
    for x in range(15):
        try:
         dic['Titel'].append(job_titel[int].text)
    
        except:
         pass

        try:
         dic['Name'].append(name_unternehmen[int].text)

        except:
         pass 
    
        try:
         dic['Zusammenfassung'].append(zusammenfassung[int].text)
    
        except:
         pass

        int +=1

    basic_url_seiten = basic_url #Url auf Standart zurücksetzen

 df = pd.DataFrame(dic)    
 return df


def csv_speichern(df):
    df.to_csv(r'PATH_to_Save_The_CSv', sep=';', encoding='utf-8')

if __name__ == '__main__':

 url = get_url("fullstack entwickler","deutschland")
 test = scrapping(url)

 csv_speichern(test)
