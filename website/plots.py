import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import folium
from flask import Flask, render_template, Blueprint, Response, send_file
from matplotlib.figure import Figure
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def countries_list():
    data_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'

    data = pd.read_csv(data_url, delimiter=',', header=0, quotechar='"', encoding="utf8", parse_dates=['date'])
    data.head()

    countries = data[['location']]
    countries = countries.drop_duplicates(subset=['location'], keep='first')
    countries = countries.values.tolist()

    flatten = lambda t: [item for sublist in t for item in sublist]
    countries = flatten(countries)

    return countries

def process_data(country):
    data_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'

    data = pd.read_csv(data_url, delimiter=',', header=0, quotechar='"', encoding="utf8", parse_dates=['date'])
    data.head()

    data = data[data['location'] == country]
    data.head()

    return data


def generate_plots(country, data):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(20, 12))

    ax1.plot(data['date'], data['new_cases'])
    # Set title and labels for axes
    ax1.set(xlabel="Date (YYYY-MM)", ylabel="New cases", title="New cases in " + country)
    ax1.grid()
    ax1.fill_between(data['date'], data['new_cases'], color=(185 / 255, 206 / 255, 255 / 255, 255 / 255))
    ax1.set_ylim(ax1.get_ylim())

    ax2.plot(data['date'], data['new_deaths'], color='black')
    # Set title and labels for axes
    ax2.set(xlabel="Date (YYYY-MM)", ylabel="New cases and deaths", title="New deaths in " + country)
    ax2.grid()
    ax2.fill_between(data['date'], data['new_deaths'], color=(0 / 255, 0 / 255, 0 / 255, 50 / 255))
    ax2.set_ylim(ax2.get_ylim())

    ax3.plot(data['date'], data['total_cases'])
    # Set title and labels for axes
    ax3.set(xlabel="Date (YYYY-MM)", ylabel="Cumulative cases", title="Cumulative cases in " + country)
    ax3.grid()
    ax3.fill_between(data['date'], data['total_cases'], color=(185 / 255, 206 / 255, 255 / 255, 255 / 255))
    ax3.set_ylim(ax3.get_ylim())

    ax4.plot(data['date'], data['total_deaths'], color='black')
    # Set title and labels for axes
    ax4.set(xlabel="Date (YYYY-MM)", ylabel="Cumulative deaths", title="Cumulative deaths in " + country)
    ax4.grid()
    ax4.fill_between(data['date'], data['total_deaths'], color=(0 / 255, 0 / 255, 0 / 255, 50 / 255))
    ax4.set_ylim(ax4.get_ylim())




    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return img









