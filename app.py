from flask import Flask, render_template, request
from forms import Questionnaire

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hey'

@app.route('/')
def homepage():
    return render_template("welcome.html")

@app.route('/info')
def info():
    return render_template("informationpage.html")

@app.route('/data', methods=['GET', 'POST'])
def data():
    form = Questionnaire()
    if request.method == 'POST':
        return "Submission completed"
    return render_template("datacollection.html", form=form)

if __name__== "__main__":
    app.run(debug=True)

