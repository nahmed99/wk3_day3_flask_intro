from app import app  #  we are importing the Flask instance called app from the file called app.py.

'''
Routes are the different URLs that the application implements. In Flask, handlers for the routes are written as Python functions, called view functions.

controller.py will deal with requests that come in to the application and determine what view functions will run based on the url that the user requests.


'''

# Decorators add extra functionality to a function in Python. The @app.route decorator creates an association between the URL and the function.
# In this example the decorator associates the URL / to this function. This means that when a web browser requests this URL, Flask is going to execute this function and pass the return value of it back to the browser as a response. 
@app.route('/')  # This is a HTTP route "decorator".
def index():
    return "Hello, world"

# To run the server...
# To run the app.py in flask, type in the following lines:
# export FLASK_APP=app.py
# flask run

# http://127.0.0.1 is the local host, so you could use 
# localhost:5000 instead of http://127.0.0.1:5000

# <ctrl>-C to stop the serve

# create a new route that will accept a paramter from the (browser) url.
# localhost:5000/name_passed_in (name_passed_in will be displayed after hello...)
@app.route('/<name>')
def hello(name):
    return f"Hello, {name}"


# NOTE: Regardless of the name we use in the url we always hit the greet route and the name is used to build up the string.
