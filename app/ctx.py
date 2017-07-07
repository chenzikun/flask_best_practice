from flask.ext.security import current_user

def user_context_processor():
    if current_user.is_authenticated():
        user = current_user._get_current_object()
    else:
        user = None
    return {
        'user': user,
    }