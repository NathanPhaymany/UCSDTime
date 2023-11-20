from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import json
import csv
import numpy as np

def scrape_subject(subject):
    url="https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudentResult.htm"
    payload = {"selectedTerm": "WI24","selectedSubjects": "CHEM"}

    request = requests.post(url, data = payload, headers = {"Content-Type": "application/x-www-form-urlencoded"})
    soup = bs(request.text, "lxml")
    table = soup.find("table", class_="tbrdr")
    rows = table.find_all("tr")
    t = []
    for row in rows:
        if (row.get("class")) == None:
            t = t + [True]
        else: 
            t = t + [False]

    print(t2)
    

scrape_subject("CHEM")
