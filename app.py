from flask import Flask, render_template, Blueprint, request, redirect, url_for
#  from first import first, html_map
from website.plots import second, create_plots, process_data, countries_list
from website import create_app

countries = countries_list()

app = create_app()
#  app.register_blueprint(first, url_prefix='')
app.register_blueprint(second, url_prefix='')

@app.route('/')
def index():
    return render_template('index.html', countries=countries)


@app.route('/plots')
def plots():
    data = process_data(country=country)
    create_plots(country=country, data=data)
    return

@app.route('/handle_data', methods=['GET', 'POST'])
def handle_data():
    global country
    country = request.form['Country']
    return redirect(url_for('plots'))

if __name__=="__main__":
    app.run(debug=True)