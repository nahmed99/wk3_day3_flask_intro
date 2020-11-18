from flask import Flask

# run the server
app = Flask(__name__)

import controller

# launch server
if __name__ == '__main__':
    app.run(debug=True)