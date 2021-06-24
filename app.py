from flask import Flask, render_template, Blueprint, request, redirect, url_for
#  from first import first, html_map
from plots import create_plots, process_data, countries_list, send_file


# get countries list depending on data source
countries = countries_list()

app = Flask(__name__)
#  app.register_blueprint(first, url_prefix='')


@app.route('/')
def index():
    return render_template('index.html', countries=countries)


@app.route('/plots')
def plots():
    return render_template('plots.html')

@app.route('/handle_plots')
def handle_plots():
    data = process_data(country=country)
    plot = create_plots(country=country, data=data)
    return send_file(plot, mimetype='img/png')


@app.route('/handle_data', methods=['GET', 'POST'])
def handle_data():
    global country
    country = request.form['Country']
    return redirect(url_for('plots'))


if __name__=="__main__":
    app.run(debug=True)