import requests
import pandas as pd
from datetime import timedelta, date

def daterange(date1, date2):
    for n in range(int((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start_dt = date(2020, 1, 22)
end_dt = date.today()
date_list = [x.strftime("%m-%d-%Y") for x in daterange(start_dt, end_dt)]

def get_files(date):
    re = requests.get("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"+date+".csv")
    print("RESPONSE: ", re.status_code, "\t DATE:", date)
    if re.status_code != 404:
        with open("data/"+date+".csv", "w", encoding="utf-8") as f: 
            f.write(re.text.replace("\r", ""))

for date in date_list:
    get_files(date)

# df = pd.read_csv(re.content.replace)