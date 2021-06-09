import numpy as np
import matplotlib.pyplot as plt
import csv
import scipy as sc
import pandas as pd
import folium
from flask import Flask, render_template


# WHO official tracked data about new cases worldwide
CASES_DATA_URL = 'https://covid19.who.int/WHO-COVID-19-global-table-data.csv'
VACCINATION_DATA_URL = 'https://covid19.who.int/who-data/vaccination-data.csv'

# headers:
# Name, WHO Region,
# Cases - cumulative total,
# Cases - cumulative total per 100000 population,
# Cases - newly reported in last 7 days,
# Cases - newly reported in last 7 days per 100000 population,
# Cases - newly reported in last 24 hours,
# Deaths - cumulative total,
# Deaths - cumulative total per 100000 population,
# Deaths - newly reported in last 7 days,
# Deaths - newly reported in last 7 days per 100000 population,
# Deaths - newly reported in last 24 hours,
# Transmission Classification
cases = pd.read_csv(CASES_DATA_URL, delimiter=',', quotechar='"', encoding="utf8", header=0)

map = folium.Map()

geoJSON_url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
country_shapes = f'{geoJSON_url}/world-countries.json'


folium.Choropleth(
    geo_data=country_shapes,
    name='choropleth COVID-19',
    data=cases,
    columns=['Name', 'Cases - cumulative total'],
    key_on='feature.properties.name',
    fill_color='YlGn',
    nan_fill_color='white'
).add_to(map)

html_map=map._repr_html_()


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', map=html_map)

if __name__=="__main__":
    app.run(debug=True)