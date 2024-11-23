from app import app
from flask import render_template


@app.route("/")
def load():
    return render_template('index.html')

@app.route("/login")
def load_test():
    return render_template('login.html')

@app.route("/register")
def load_register_form():
    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)
