from flask_login import current_user

def author_context_processor():
    return {
        'author': "chenzikunczk@gmail.com",
    }


