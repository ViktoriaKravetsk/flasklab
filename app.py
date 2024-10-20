from flask import Flask, request, redirect, url_for

app = Flask(__name__)
app.config.from_pyfile("config.py")
@app.route('/')
def hello():
    return "Hello, World!", 200

@app.route('/homepage')
def homepage():
    agent = request.user_agent
    return f"Welcome to the homepage! - {agent}"

@app.route("/hi/<string:name>")
def greetings(name):
    name = name.upper()
    age = request.args.get("age", default=0, type=int)
    year = 2024 - age
    return f"Welcome, {name} - {year}"

@app.route('/admin')
def admin():
    to_url = url_for("greetings", name="administrator", age=45, _external=True)
    print(to_url)
    return redirect(to_url)

if __name__ == '__main__':  # Змінено name на __name__
    app.run(debug=True)
