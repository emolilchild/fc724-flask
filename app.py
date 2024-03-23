from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("welcome.html")

@app.route('/info')
def info():
    return render_template("informationpage.html")

@app.route('/form')
def form():
    return render_template("datacollection.html")

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    return f"Hello {username}! Thank you for submitting the form!"

if __name__== "__main__":
    app.run(debug=True)

