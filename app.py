from flask import Flask

# run the server
app = Flask(__name__)

# launch server
if __name__ == '__main__':
    app.run(debug=True)