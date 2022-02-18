# Creating the Flask app
from flask import Flask
app = Flask(__name__)

# Creating the first route
@app.route('/') # <-- the forward slash denotes that we want
                #     to put our data at the root of our routes.
                #     This is known as the highest level of hierarchy.

def hello_world(): # <-- creating a 'hello_world' function
    return 'Hello World'

@app.route('/link')
def i_am_cool():
    return 'such wow!'