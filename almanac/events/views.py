from pyramid.view import view_config

from almanac.models import Event
@view_config(route_name='event.list', renderer="events/list.html")
def list(request):
    events = Event.query.order_by(Event.start_time.desc())
    return {'events': events}
