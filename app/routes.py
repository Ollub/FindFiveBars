from flask import render_template, redirect, request, url_for

from app import app
from app.forms import LocationForm
from app.map import create_bars_map
from app.bars_geo import fetch_bars_geo


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index(location='Reutov'):
    if request.method == 'POST' and request.form.get('location'):
        location = request.form.get('location')
    bars_geo = fetch_bars_geo(location) #read json file and define distances
    create_bars_map(location, bars_geo[:5])
    return render_template('index.html', title='Bars_map', location=location)