from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import json
import csv
import numpy as np
import time

def scrape_subject(subject, page):

    #Requesting the URL
    url=f"https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudentResult.htm?page={page}"
    payload = {"selectedTerm": "WI24","selectedSubjects": subject}

    request = requests.post(url, data = payload, headers = {"Content-Type": "application/x-www-form-urlencoded"})
    soup = bs(request.text, "lxml")


    table = soup.find("table", class_="tbrdr")
    rows = table.find_all("tr")

    #Finds where courses are divided
    indexes_of_rows_with_no_class = []
    counter = 0
    for row in rows:
        if (row.get("class")) == None:
            indexes_of_rows_with_no_class = indexes_of_rows_with_no_class + [counter]
        counter = counter + 1
    
    indexes_of_course_dividers = [0]+[i for i in indexes_of_rows_with_no_class if i+1 not in indexes_of_rows_with_no_class]
    breaks = ["FI", "DI", "MI", "LE", "LA"]
    splits = [rows[indexes_of_course_dividers[i]:indexes_of_course_dividers[i+1]] for i in range(0, len(indexes_of_course_dividers) - 1 )]


    temp = []
    for split in splits:
        z=[]
        for tds in split:
            for td in tds:
                z = z + [td.text.replace('\t', '').replace('\n', '').replace('\r', '').replace('\xa0', '').replace(' ', '')]
        
        z = list(filter(None, z))
        t2 = list()
        t3 = list()
        for item in z:
            if item in breaks:
                t3.append(t2)
                t2 = []
                t2.append(item)
            else:
                t2.append(item)
        t3.append(t2)
        data = list()

        course_name = ""
        course_desc = ""
        for i in t3:
            if i[0] not in breaks:
                course_name = i[0]
                course_desc = i[1]
            else:
                data.append(i)
        t4 = {"course_name": course_name, "course_description": course_desc, "data": data}
        temp.append(t4)

    return temp

    

if __name__ == "__main__":
    subject_list = json.load(open("/Users/darren/Desktop/dev/UCSDTime/subjects.json", "r"))["codes"]

    ret = {}
    for subject in ["MATH"]:
        a = []
        for i in range(0, 20):
            try:
                a.append(scrape_subject(subject, i))
            except: 
                ret[subject] = a
        time.sleep(1)
    print(ret)
    with open("/Users/darren/Desktop/dev/UCSDTime/test.json", "w") as outfile:
        outfile.write(json.dumps({"data": ret}, indent=4))
