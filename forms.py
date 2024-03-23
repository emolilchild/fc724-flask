from wtforms import Form, StringField

class Questionnaire:
    f_name = StringField(label="f_name", validators=[DataRequired()])
    l_name = StringField(label="l_name", validators=[DataRequired()])