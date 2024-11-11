from app import app

@app.route('/users')
def users():
    return "List of users"
