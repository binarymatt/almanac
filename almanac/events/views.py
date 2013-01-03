from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from almanac.models import Event

@view_config(route_name='event.list', renderer="events/list.html")
@view_config(route_name='events.ics')
def list(request):
    events = Event.query.order_by(Event.start_time.desc())
    return {'events': events}

@view_config(route_name='event.detail', renderer="events/detail.html")
def detail(request):
    event_id = request.matchdict.get('id')
    event = Event.query.get(event_id)
    if not event:
        return HTTPNotFound('')
    return {'event': event}
