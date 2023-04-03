from app import app, db
from app.models import ArchivesCrusherComment
from datetime import datetime


with app.app_context():
    try:
        filled = ArchivesCrusherComment.get_unfilled_comments()
        print(f"Empty msgs objects:\n")
        for r in filled:
            print(r)
    except Exception as e:
        print(f"Getting empty msgs fails with {e}")


with app.app_context():
    try:
        filled = ArchivesCrusherComment.get_filled_comments()
        print(f"filled msgs objects:\n")
        for r in filled:
            print(r)
    except Exception as e:
        print(f"Getting filled msgs fails with {e}")


date = datetime(2005, 7, 14, 12, 30)
print(date.strftime("%d.%m.%Y %H:%M"))