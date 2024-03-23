from flask import Flask, render_template, request
from forms import Questionnaire
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
    form = Questionnaire()
    if form.validate_on_submit():
        username = request.form['f_name']
        return f"Hello {username}! Thank you for submitting the form!"
    else:
        return "Invalid submission. Please try again."

if __name__== "__main__":
    app.run(debug=True)

