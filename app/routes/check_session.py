from flask import request
from . import routes

from atom import Atom, views

@routes.route('/check-session', methods=['GET'], endpoint='check_session')
@Atom.apply(view=views.signed_in)
def check_session():
    print(request.user.id)
    print(request.args.get('test'))
    return '', 200