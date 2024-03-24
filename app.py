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
    if form.validate_on_submit():
        with open('collected_data.txt', 'a') as f:
            f.write(f"First name: {form.f_name.data\n}")
            f.write(f"Last name: {form.l_name.data\n}")
            f.write(f"Student number: {form.student_number.data\n}")
            f.write(f"Email: {form.email.data\n}")
            f.write(f"Question 1: {form.qn_one.data\n}")
            f.write(f"Question 2: {form.qn_two.data\n}")
            f.write(f"Question 3: {form.qn_three.data\n}")
            f.write(f"Question 4: {form.qn_four.data\n}")
            f.write(f"Question 5: {form.qn_five.data\n}")
            f.write(f"Question 6: {form.qn_six.data\n}")
            f.write(f"Question 7: {form.seven.data\n}")
            f.write(f"Question 8: {form.qn_eight.data\n}")
            return "Submission completed"
    return "Invalid Submission"

if __name__== "__main__":
    app.run(debug=True)

