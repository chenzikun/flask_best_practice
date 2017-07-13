from functools import wraps
from flask import (
    g, redirect, url_for, request, render_template
)
from werkzeug.contrib.cache import SimpleCache

#: flask-login有现成模块
def login_required(f):
    """登录装饰器"""

    @wraps(f)
    def decorated_func(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return f(*args, **kwargs)
    return decorated_func


cache = SimpleCache()


def cached(timeout=5 * 60, key="view/{}"):
    """缓存装饰器"""

    def decorator(f):
        @wraps(f)
        def decorated_func(*args, **kwargs):
            cache_key = key.format(request.path)
            rv = cache.get(cache_key)
            if rv is not None:
                return rv
            rv = f(*args, **kwargs)
            cache.set(cache_key, rv, timeout=timeout)
            return rv
        return decorated_func
    return decorator


def templated(template=None):
    """
    模板装饰器
    demo:
        @app.route('/')
        @templated('index.html')
        def index():
            return dict(value=42)
    """

    def decorator(f):
        @wraps(f)
        def decorated_func(*args, **kwargs):
            template_name = template
            if template is None:
                template_name = request.endpoint.replace(".", "/") + ".html"
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)
        return decorated_func
    return decorator
