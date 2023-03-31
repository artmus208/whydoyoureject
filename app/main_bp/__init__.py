import click
from flask import (
    Blueprint, render_template, redirect, url_for, request
    )

from app.forms import TestForm, ACCForm


from app import logger, db
from app.models import ArchivesCrusherComment
main = Blueprint('main', __name__, static_url_path="/static/main", static_folder="/static/main")

@main.cli.command("create_db")
def create_db():
    print("Creating models...")
    db.create_all()

@main.cli.command("drop_db")
def create_db():
    print("Droping models...")
    db.drop_all()

@main.cli.command("add_msg")
@click.argument("msg")
def add_msg(msg=None):
    try:
        ArchivesCrusherComment(msg).save()
        logger.info(f"Msg: {msg} added in DB.")
    except Exception as e:
        logger.exception(f"Add msg fails with {e}")
    
@main.cli.command("add_empty_msg")
def add_empty_msg():
    try:
        ArchivesCrusherComment().save()
        msg_for_log = "Empty msg added in DB."
        
        print(msg_for_log)
        logger.info(msg_for_log)
    except Exception as e:
        msg_for_log = f"Add empty msg fails with {e}"

        print(msg_for_log)
        logger.exception(msg_for_log)
