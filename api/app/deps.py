from .db import SessionLocal
from contextlib import contextmanager

@contextmanager
def session_scope():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except:  # noqa
        db.rollback()
        raise
    finally:
        db.close()

def get_db():
    with session_scope() as s:
        yield s
