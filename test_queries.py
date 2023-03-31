from app import app, db
from app.models import ArchivesCrusherComment

with app.app_context():
    try:
        empty = ArchivesCrusherComment.get_unfilled_comments()
        print(f"Empty msgs objects:\n {empty.all()}")
    except Exception as e:
        print(f"Getting empty msgs fails with {e}")
