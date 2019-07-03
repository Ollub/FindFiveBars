from flask import render_template, redirect

from app import app
from app.forms import LocationForm
from app.map import create_bars_map
from app.bars_geo import fetch_bars_geo


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():    
    form = LocationForm()
    if form.validate_on_submit():
        location = form.location.data
        print(location)
    else:
        location = 'Reutov'
        # bars_geo = fetch_bars_geo(location)
        # create_bars_map(location, bars_geo)
        # return render_template('index.html', form=form, title='Bars_map', location=location)
    bars_geo = fetch_bars_geo(location)
    create_bars_map(location, bars_geo)
    return render_template('index.html', form=form, title='Bars_map', location=location)
