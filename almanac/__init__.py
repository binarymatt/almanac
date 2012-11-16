import os
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .models import initialize_sql
from .models import (
    DBSession,
    Base,
)

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    #database_url = os.environ.get('DATABASE_URL')
    #if database_url:
    #    settings['sqlalchemy.url'] = database_url
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    #DBSession.configure(bind=engine)
    #Base.metadata.bind = engine
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

