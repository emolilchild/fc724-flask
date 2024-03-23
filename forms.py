from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, Email
class Questionnaire:
    f_name = StringField(label="f_name", validators=[DataRequired()])
    l_name = StringField(label="l_name", validators=[DataRequired()])
    student_number = IntegerField(label="student_number", validators=DataRequired())
    