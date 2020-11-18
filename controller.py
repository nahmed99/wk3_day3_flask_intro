from app import app

@app.route('/')  # This is a HTTP route
def index():
    return "Hello, world"

# To run the server...
# To run the app.py in flask, type in the following lines:
# export FLASK_APP=app.py
# flask run

# http://127.0.0.1 is the local host, so you could use 
# localhost:5000 instead of http://127.0.0.1:5000

# <ctrl>-C to stop the serve


# localhost:5000/name_passed_in
@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}"

