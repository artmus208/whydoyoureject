
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, FieldList, FormField
from wtforms.validators import Length
from app.models import ArchivesCrusherComment
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
    # def __init__(self, label):
    #     self.comment.label = label

class ACCFormList(FlaskForm):
    comments = FieldList(FormField(ACCForm))
    submit = SubmitField("Отправить причины отказа")

    def make_list(self, unfilled_comments):
        n = len(unfilled_comments)
        for i in range(n):
            self.comments.append_entry()
        if unfilled_comments:
            for i in range(n):
                label = f"Заполните причину отказа от \
                    {unfilled_comments[i].time_created}, \
                    с номером дробилки: {unfilled_comments[i].crusher_id}"
                self.comments[i].comment.label = label  


    
    

