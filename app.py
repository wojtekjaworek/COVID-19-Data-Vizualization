from flask import Flask, render_template, Blueprint, request, redirect, url_for, send_file
#  from first import first, html_map
from website.plots import generate_plots, process_data, countries_list
from website import create_app
from website.world_map import options_list, create_world_map

countries = countries_list()
options = options_list()

app = create_app()


@app.route('/')
def index():

    world_map = create_world_map()
    return render_template('index.html', countries=countries, options=options, world_map=world_map)


@app.route('/plots')
def plots():
    return render_template('plots.html', countries=countries, options=options)

@app.route('/create_plots')
def create_plots():
    data = process_data(country=country)
    plot = generate_plots(country=country, data=data)
    return send_file(plot, mimetype='img/png')

@app.route('/get_country_for_plots', methods=['GET', 'POST'])
def get_country_for_plots():
    global country
    country = request.form['Country']
    return redirect(url_for('plots'))


@app.route('/get_option_for_map', methods=['GET', 'POST'])
def get_option_for_map():

    option = request.form['Get_option_for_map']
    return redirect(url_for('/'))

if __name__=="__main__":
    app.run(debug=True)