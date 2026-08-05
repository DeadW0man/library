from flask import request
from app.repository.repository import get_user_by_session_id
from app.schemas.schemas import UserResponse, BookResponse, ShareResponse

def validate_session_id(session_id):
    if not session_id:
        return False
    return get_user_by_session_id(session_id) is not None

def is_auth_valid():
    session_id = request.headers.get('SessionID')
    if session_id:
        return validate_session_id(session_id)
    return False

def get_current_user():
    session_id = request.headers.get('SessionID')
    if not session_id:
        return None
    return get_user_by_session_id(session_id)

def user_row_to_dict(row):
    if not row:
        return None
    return UserResponse(id=row[0], name=row[1], email=row[2]).model_dump()

def book_row_to_dict(row):
    if not row:
        return None
    return BookResponse(id=row[0], title=row[1], author=row[2], release_year=row[3], owner_id=row[4]).model_dump()

def share_row_to_dict(row):
    if not row:
        return None
    return ShareResponse(id=row[0], book_id=row[1], giver_id=row[2], taker_id=row[3], final_date=row[4]).model_dump()
