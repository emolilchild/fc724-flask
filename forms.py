from wtforms import Form, StringField, IntegerField, SelectField, RadioField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length
class Questionnaire(Form):
    f_name = StringField(label="f_name", validators=DataRequired())
    l_name = StringField(label="l_name", validators=DataRequired())
    student_number = IntegerField(label="student_number", validators=[DataRequired(),Length(min=6, max=6)])
    email = StringField(label="email", validators=[DataRequired(), Email()])
    qnone = SelectField(label="qnone", validators=DataRequired())
    qntwo = RadioField(label="qntwo", validators=DataRequired(), choices=[("a", "A"), ("b", "B"), ("c", "C"), ("d","D"), ("e", "E"), ("f", "F")])
    qnthree = TextAreaField(label="qnthree", validators=DataRequired())
    qn_four = IntegerField(label="qn_four", validators=DataRequired())
    qn_five = TextAreaField(label="qnfive", validators=DataRequired())
    qn_six = BooleanField(label="qnsix", validators=DataRequired(), choices=[("teacher", "Teacher"), ("friend", "Friends"), ("location", "Location"), ("curriculum", "Curriculum")])
    qn_seven = TextAreaField(label="qnseven", validators=DataRequired())
    qn_eight = RadioField(label="qntwo", validators=DataRequired(), choices=[("very good", "Very Good"), ("good", "Good"), ("neutral", "Neutral"), ("bad", "Bad"), ("very bad", "Very Bad")])
    button = SubmitField(label="submit")