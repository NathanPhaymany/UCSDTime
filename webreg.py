import csv
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


website = 'https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudentResultPrint.htm'

'''
page = urlopen(website).read()
soup = BeautifulSoup(page, 'html.parser')

print(soup)
'''

br = webdriver.Chrome()
br.implicitly_wait(0.5)
br.get(website)

subjectSelect = Select(br.find_element(By.ID, 'selectedSubjects'))
subjectSelect.select_by_value('AAS ')
select = br.find_element(By.ID, 'socFacSubmit')
br.execute_script('arguments[0].click();', select)

print(br.title)

time.sleep(15)
br.quit()