from functools import wraps
from flask import request, redirect, session

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("id") is None:
            return redirect('/login')
        return f(*args, **kwargs)
    
    return decorated_function