
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import Length

class TestForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    about = TextAreaField("About you")
    submit = SubmitField("Сохранить")

# TODO:
# [ ]: Сделать функцию инициализации списка полей для комментариев 
# (может создать новый объект)
# [ ]: Добавить поля для информации о дробилке и даты/времени


class ACCForm(FlaskForm):
    comment = TextAreaField("Ваша причина, сэр:",
                            validators=[Length(min=1, max=255)]
                            )
    submit = SubmitField("Сохранить")
    list_of_comments = list()

    def make_list_of_comments():
        pass


    
    

