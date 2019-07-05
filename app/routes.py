from flask import render_template, redirect, request, url_for, flash

from app import app
from app.map import create_bars_map
from app.bars_geo import fill_bars_geo


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index(location='Reutov'):
    if request.method == 'POST' and request.form.get('location'):
        location = request.form.get('location')
    try:
        bars_geo = fill_bars_geo(location)
        create_bars_map(location, bars_geo[:5])
    except:
        flash('Something goes wrong')
    return render_template('index.html', title='Bars_map', location=location)