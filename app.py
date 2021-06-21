import numpy as np
import matplotlib.pyplot as plt
import csv
import scipy as sc
import pandas as pd
import folium
from flask import Flask, render_template, Blueprint
import cartopy as cp
from first import first, html_map
from second import second

app = Flask(__name__)
app.register_blueprint(first, url_prefix='')
app.register_blueprint(second, url_prefix='')

@app.route('/')
def index():
    return render_template('index.php')

if __name__=="__main__":
    app.run(debug=True)