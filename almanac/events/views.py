from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from almanac.models import Event
from sqlalchemy import func
from sqlalchemy import Date, cast

@view_config(route_name='event.list', renderer="events/list.html")
@view_config(route_name='events.ics')
def list(request):
    events = Event.query.filter(cast(Event.start_time, Date) >= func.current_date()).order_by(Event.start_time.asc())
    return {'events': events}

@view_config(route_name='event.detail', renderer="events/detail.html")
def detail(request):
    event_id = request.matchdict.get('id')
    event = Event.query.get(event_id)
    if not event:
        return HTTPNotFound('')
    return {'event': event}

@view_config(route_name='event.new', renderer='events/new.html')
def new(request):
    return {}
