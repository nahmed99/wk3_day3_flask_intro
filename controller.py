from app import app

@app.route('/')  # This is a HTTP route
def index():
    return "Hello, world"