from . import *

@main.get("/")
def index():
    logger.info(f"Index page says 'Hello!'")
    return render_template("reject/index.html")

@main.get("/reject-form")
def reject_form():
    return render_template("reject/reject_form.html")