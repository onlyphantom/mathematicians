"""Flask routing.
Specifying routes for our Flask app is simple. We do it just by providing
the desired route in the `@app.route()` decorator. Sometimes our routes have
dynamic parameters. For example:
* `/posts/23` -> The number 23 (post id) is dynamic
* `/repo/flask-introduction/stars` -> The name of the repo (flask-introduction)
                                      is dynamic
Supporting dynamic routing parameters is really simple. We just need to
specify the desired dynamic portion by giving it a name and surrounding
it between `<>`.
"""

from flask import Flask, render_template

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

@app.route('/person/<person_last_name>')
def person(person_last_name):
    return render_template('routing/mathematician.html', 
                person = mathematicians_dict[person_last_name]
            )
