from flask import Flask, render_template, abort, request, redirect, url_for
import requests

app = Flask(__name__)

mathematicians_dict = {
    'poe': {
        'full_name': 'Edgar Allan Poe',
        'nationality': 'US',
        'notable_work': 'The Raven',
        'born': 'January 19, 1809',
        'picture': 'https://upload.wikimedia.org/wikipedia/commons/2/27/Edgar_Allan_Poe_2.jpg'
    },
    'borges': {
        'full_name': 'Jorge Luis Borges',
        'nationality': 'Argentine',
        'notable_work': 'The Aleph', 
        'born': 'August 24, 1899',
        'picture': 'https://images.gr-assets.com/authors/1496948506p5/500.jpg'
    }
}

@app.route('/')
def index():
    return render_template('routing/mathematicians.html')

@app.route('/person/<string:person_last_name>')
def person(person_last_name):
    if person_last_name not in mathematicians_dict:
        abort(404)
    return render_template('routing/mathematician.html',
                person = mathematicians_dict[person_last_name])

@app.route('/person/<string:person_last_name>/edit')
def person_admin(person_last_name):
    abort(401)

@app.route('/request-info')
def request_info():
    # Get location info using https://freegeoip.net
    geoip_url = 'https://freegeoip.net/json/{}'.format(request.remote_addr)
    client_location = requests.get(geoip_url).json()
    return render_template('request/info.html', client_location = client_location)

# temporarily redirect; by default `redirect()` is 302
@app.route('/redirect-me')
def redirect_me():
    return redirect(url_for('request_info'))

# permanently redirect with a 301
@app.route('/info')
def info():
    return redirect(url_for('request_info'), code=301)

@app.errorhandler(404)
def not_found(error):
    return render_template('routing/404.html'), 404
