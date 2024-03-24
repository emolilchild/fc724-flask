from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, RadioField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Optional



class Questionnaire(FlaskForm):
    f_name = StringField(label="First Name", validators=[DataRequired()])
    l_name = StringField(label="Last Name", validators=[DataRequired()])
    student_number = IntegerField(label="Student Number", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired()])
    qn_one = SelectField(label="Q1: What course do you take here in GIC?", validators=[DataRequired()], choices=[("FCsciandeng", "FC Science and Engineering"),
                                                                                    ("FCbuisandmanage", "FC Buisness and Management"),
                                                                                    ("PMsciandeng", "PM Science and Engineering"),
                                                                                    ("PMbuisandmanage", "PM Buisness and Management")])
    qn_two = RadioField(label="What grade did you get for last semester?", validators=[DataRequired()],
                       choices=[("1", "A"), ("2", "B"), ("3", "C"), ("4","D"), ("5", "E"), ("6", "F")])

    qn_three = TextAreaField(label="Q3: How do you feel about the grade you have obtained?", validators=[DataRequired()])
    qn_four = StringField(label="Q4: How satisfied are you with your academic experience here in GIC?")
    qn_five = TextAreaField(label="Q5: Is there anything you would change about the curriculum?", validators=[DataRequired()])
    teachers = BooleanField(label="Teachers", validators=[Optional()])
    friends = BooleanField(label="Friends", validators=[Optional()])
    location = BooleanField(label="Location", validators=[Optional()])
    curr = BooleanField(label="Curriculum", validators=[Optional()])
    qn_seven = TextAreaField(label="Q7: Is there any other feedback you would like to add?", validators=[DataRequired()])
    qn_eight = RadioField(label=" Q8: How would you rate this questionnaire?", validators=[DataRequired()],
                          choices=[("1", "Very Good"), ("2", "Good"), ("3", "Neutral"), ("4", "Bad"), ("5", "Very Bad")])
    submit = SubmitField(label="Submit")