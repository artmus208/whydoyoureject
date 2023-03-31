from . import *

@main.get("/")
def index():
    logger.info(f"Index page says 'Hello!'")
    return render_template("reject/index.html")

@main.get("/reject-form")
def reject_form():
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