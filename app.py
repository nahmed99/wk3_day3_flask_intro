from flask import Flask

# To run the server...
# To run the app.py in flask, type in the following lines:
# export FLASK_APP=app.py
# flask run

# http://127.0.0.1 is the local host, so you could use 
# localhost:5000 instead of http://127.0.0.1:5000

# <ctrl>-C to stop the serve


# create an instance of Flask
app = Flask(__name__)

import controller

# 
if __name__ == '__main__':
    app.run(debug=True)