from flask import Blueprint
from flask.views import MethodView
from flask.views import View

from flask import render_template


view_bp = Blueprint("view", __name__, url_prefix="view")


class ListView(View):

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = {'objects': self.get_objects()}
        return self.render_template(context)

    def get_objects(self):
        pass

class UserView(ListView):

    def get_template_name(self):
        return 'users.html'

    def get_objects(self):
        return "User.query.all()"


class UserAPI(MethodView):

    def get(self):
        pass

    def post(self):
        pass

view_bp.add_url_rule('/users/', view_func=UserAPI.as_view('users'))
