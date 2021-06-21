import numpy as np
import matplotlib.pyplot as plt
import csv
import scipy as sc
import pandas as pd
import folium
from flask import Flask, render_template, Blueprint
import cartopy as cp
import matplotlib.ticker as ticker
import datetime

# WHO official tracked data about new cases worldwide
CASES_FROM_3RD_JANUARY_URL = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'
CASES_DATA_URL = 'https://covid19.who.int/WHO-COVID-19-global-table-data.csv'
VACCINATION_DATA_URL = 'https://covid19.who.int/who-data/vaccination-data.csv'




cases = pd.read_csv(CASES_DATA_URL, delimiter=',', quotechar='"', encoding="utf8", header=0)
cases_from_3rd_january = pd.read_csv(CASES_FROM_3RD_JANUARY_URL, delimiter=',', quotechar='"', encoding="utf8", header=0)


collect_date = []
collect_cases = []


# for record in cases_from_3rd_january.iterrows():
#     if record[1]['Country'] == get_country:
#         collect_cases.append(record[1]['New_cases'])
#         collect_date.append(np.datetime64(record[1]['Date_reported']))
#


plt.plot_date(collect_date, collect_cases, 'r-')
plt.grid()
plt.show()



second = Blueprint('second', __name__, static_folder='Static', template_folder='Templates')





@second.route('/second')
def index():
    return render_template('index.html')











