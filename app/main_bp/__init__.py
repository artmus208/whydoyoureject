from flask import (
    Blueprint, render_template, redirect, url_for, request
    )

from app import logging
main = Blueprint('main', __name__, static_url_path="/static/main", static_folder="/static/main")
# Конфигурация логгера
def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    file_handler = logging.FileHandler("app.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
logger = setup_logger()