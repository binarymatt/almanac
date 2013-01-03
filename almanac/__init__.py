import os
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from almanac.models import initialize_sql

class ICSRendererFactory(object):
    def __init__(self, info):
        """ Constructor: info will be an object having the
        following attributes: name (the renderer name), package
        (the package that was 'current' at the time the
        renderer was registered), type (the renderer type
        name), registry (the current application registry) and
        settings (the deployment settings dictionary). """
        self._info = info

    def __call__(self, value, system):
        """ Call the renderer implementation with the value
        and the system value passed in as arguments and return
        the result (a string or unicode object).  The value is
        the return value of a view.  The system value is a
        dictionary containing available system values
        (e.g. view, context, and request). """
        result = value
        return result

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    database_url = os.environ.get('ALMANAC_DATABASE_URL')
    if database_url:
        settings['sqlalchemy.url'] = database_url
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    config = Configurator(settings=settings)
    config.add_tween('pyramid_spine.tweens.timezone_tween_factory')
    config.include('pyramid_jinja2')
    config.add_renderer('.html', factory='pyramid_jinja2.renderer_factory')
    config.add_jinja2_search_path("almanac:templates")

    config.include('almanac.events', route_prefix="/events")
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()

    return config.make_wsgi_app()

