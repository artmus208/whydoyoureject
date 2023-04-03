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
    form = ACCFormList()
    unfilled_comments = ArchivesCrusherComment.get_unfilled_comments()
    form.make_list(unfilled_comments)
    return render_template("reject/reject_form.html", forms=form)
    # return f"Count of forms:{len(form.forms)}, count of unfilled comments: {len(unfilled_comments)}"


# [ ]: Надо принять список заполненных сообщений (в виде массива!)
# TIPS: Для того, чтобы это сделать надо воспользоваться Flask-WTF
# создать свой виджет. В нём будет содержаться список полей textarea.
@main.post("/reject-form")
def reject_form_post():
    logger.info(f"Index reject_form.post says 'Hello!'")
    unfilled_comments = ArchivesCrusherComment.get_unfilled_comments()
    form = ACCFormList()
    print(form.errors)
    for ix, c in enumerate(form.comments):
        unfilled_comments[ix].comment = c.comment.data
        unfilled_comments[ix].commit()
    journal = ArchivesCrusherComment.get_filled_comments()
    for j in journal:
        print(j.as_dict())
    return "Test dict"
    # return render_template("reject/reject_form.html", forms=None, journal=journal)












@main.get("/services")
def reject_services():
    return render_template("reject/services.html")

@main.get("/blog")
def reject_blog():
    return render_template("reject/blog.html")

@main.get("/products")
def reject_products():
    return render_template("reject/products.html")
