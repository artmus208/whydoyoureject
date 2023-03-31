from . import *

@main.get("/")
def index():
    logger.info(f"Index page says 'Hello!'")
    return render_template("reject/index.html")

@main.get("/reject-form")
def reject_form():
    logger.info(f"Index reject_form.get says 'Hello!'")
    return render_template("reject/reject_form.html")



# TODO:
# [ ]: Создать в модель в БД
# [ ]: Сделать проверку записей
@main.post("/reject-form")
def reject_form_post():
    logger.info(f"Index reject_form.post says 'Hello!'")
    logger.debug(f"Reason: {request.form.get('why','Fail why')}")
    return redirect(url_for("main.index"))
