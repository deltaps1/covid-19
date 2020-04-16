import requests
import pandas as pd
from matplotlib import pyplot

def get_ecdc_data():
    ecdc_data = "https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-04-07.xlsx"

    with requests.Session() as s: 
        data = s.get(ecdc_data).content
    return pd.read_excel(data)

