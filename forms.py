from wtforms import Form, StringField, IntegerField, SelectField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
class Questionnaire(Form):
    f_name = StringField(label="f_name", validators=DataRequired())
    l_name = StringField(label="l_name", validators=DataRequired())
    student_number = IntegerField(label="student_number", validators=[DataRequired(),Length(min=6, max=6)])
    email = StringField("email", validators=[DataRequired(), Email()])
    qnone = SelectField(label="qnone", validators=DataRequired())
    qntwo = RadioField(label="qntwo", validators=DataRequired())
    qnthree = TextAreaField(label="qnthree", validators=DataRequired())
    qn_four = IntegerField(label="qn_four", validators=DataRequired())
    qn_five = TextAreaField(label="qnthree", validators=DataRequired())