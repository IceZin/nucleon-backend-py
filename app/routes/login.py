from flask import make_response, request
from . import routes
from datetime import datetime, timedelta

from models import Session, UserQueries, SessionQueries

@routes.route('/import', methods=['POST'], endpoint='import')
def import_csv():
    data = request.get_json()

    print(data)

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return '', 400
    
    user = UserQueries.get_by_username(username)

    print(user.email)

    if not user:
        return '', 400
    
    if user.password != password:
        return '', 400
    
    print(user.uuid)

    session = Session(
       user_uuid=user.uuid,
       active=True,
       expires_at=datetime.now() + timedelta(days=7)
    )

    session_uuid = SessionQueries.insert(session)

    if session_uuid:
        response = make_response('')
        response.set_cookie("user", str(user.uuid))
        response.set_cookie("session", str(session_uuid))
        return response
    else:
        return '', 500