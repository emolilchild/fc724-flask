from wtforms import Form, StringField, IntegerField, SelectField, RadioField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length
class Questionnaire(Form):
    f_name = StringField(label="First Name", validators=[DataRequired()])
    l_name = StringField(label="Last Name", validators=[DataRequired()])
    student_number = IntegerField(label="Student Number", validators=[DataRequired(),Length(min=6, max=6)])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    qnone = SelectField(label="Q1: What course do you take here in GIC?", validators=[DataRequired()], choices=[("FCsciandeng", "FC Science and Engineering"),
                                                                                    ("FCbuisandmanage", "FC Buisness and Management"),
                                                                                    ("PMsciandeng", "PM Science and Engineering"),
                                                                                    ("PMbuisandmanage", "PM Buisness and Management")])



    qntwo = RadioField(label="What grade did you get for last semester?", validators=[DataRequired()],
                       choices=[("1", "A"), ("2", "B"), ("3", "C"), ("4","D"), ("5", "E"), ("6", "F")])

    qnthree = TextAreaField(label="qnthree", validators=[DataRequired()])
    qn_four = IntegerField(label="qnfour", validators=[DataRequired()])
    qn_five = TextAreaField(label="qnfive", validators=[DataRequired()])
    qn_six = BooleanField(label="qnsix", validators=[DataRequired()])
    qn_seven = TextAreaField(label="qnseven", validators=[DataRequired()])
    qn_eight = RadioField(label="qntwo", validators=[DataRequired()], choices=[("very good", "Very Good"), ("good", "Good"), ("neutral", "Neutral"), ("bad", "Bad"), ("very bad", "Very Bad")])
    submit = SubmitField(label="submit")