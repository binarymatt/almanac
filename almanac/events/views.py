import datetime
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from almanac.models import Event, Venue
from almanac.events.forms import EventForm
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
    start_ts = datetime.datetime.now()
    end_ts = start_ts + datetime.timedelta(hours=1)
    form = EventForm(request.POST, start_time=datetime.datetime.now(), end_time=end_ts)
    if request.method == "POST" and form.validate():
        pass
    venues = [venue.title for venue in Venue.query.all()]
    return {'form': form, 'venues': venues}

@view_config(route_name='event.add', renderer='events/add.html')
def add(request):
    return {}
