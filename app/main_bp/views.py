from . import *

@main.get("/")
def index():
    logger.info(f"Index page says 'Hello!'")
    return render_template("reject/index.html")

# TODO:
# [ ]: Получить здесь список всех пустых записей из БД
# [ ]: Выдать их на страницу
# @main.route("/reject-form", methods=["POST", "GET"])
@main.get("/reject-form")
def reject_form_get():
    logger.info(f"Index reject_form.get says 'Hello!'")
    form = ACCForm()
    list_of_empty_projects = ArchivesCrusherComment.get_unfilled_comments()
    
    return render_template("reject/reject_form.html", form=form)


# [ ]: Надо принять список заполненных сообщений (в виде массива!)
# TIPS: Для того, чтобы это сделать надо воспользоваться Flask-WTF
# создать свой виджет. В нём будет содержаться список полей textarea.
@main.post("/reject-form")
def reject_form_post():
    logger.info(f"Index reject_form.post says 'Hello!'")
    logger.debug(f"Reason: {request.form.get('why','Fail why')}")
    form = ACCForm()
    print(form.errors)
    print(form.comment.data)
    return render_template("reject/reject_form.html", form=None)












@main.get("/services")
def reject_services():
    return render_template("reject/services.html")

@main.get("/blog")
def reject_blog():
    return render_template("reject/blog.html")

@main.get("/products")
def reject_products():
    return render_template("reject/products.html")
