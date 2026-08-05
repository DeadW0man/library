from flask import request
from app.repository.repository import get_user_by_session_id

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
