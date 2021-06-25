from flask import Flask, render_template, Blueprint, request, redirect, url_for
from world_map import world_map, options_list
from plots import create_plots, process_data, countries_list, send_file


# get countries list depending on data source
countries = countries_list()
world_map_options = options_list()

app = Flask(__name__)
#  app.register_blueprint(first, url_prefix='')


@app.route('/')
def index():
    try: # try pass argument, in case it is not defined run with default arguments
        map = world_map(option=world_map_picked_option)
        return render_template('index.html', countries=countries, map=map, world_map_options=world_map_options,
                               world_map_picked_option=world_map_picked_option)

    except:
        map = world_map()
        return render_template('index.html', countries=countries, map=map, world_map_options=world_map_options)



@app.route('/plots')
def plots():
    return render_template('plots.html', countries=countries, country=country)

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


@app.route('/handle_world_map', methods=['GET', 'POST'])
def handle_world_map():
    global world_map_picked_option
    world_map_picked_option = request.form['world_map_option']
    return redirect(url_for('index'))


if __name__=="__main__":
    app.run(debug=True)