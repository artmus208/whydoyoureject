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
# [X]: Создать в модель в БД
# [ ]: Сделать проверку записей
@main.post("/reject-form")
def reject_form_post():
    logger.info(f"Index reject_form.post says 'Hello!'")
    logger.debug(f"Reason: {request.form.get('why','Fail why')}")
    return render_template("reject/reject_form.html")

@main.get("/services")
def reject_services():
    return render_template("reject/services.html")

@main.get("/blog")
def reject_blog():
    return render_template("reject/blog.html")

@main.get("/products")
def reject_products():
    return render_template("reject/products.html")
