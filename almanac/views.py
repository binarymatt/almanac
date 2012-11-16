from datetime import timedelta, datetime
from pyramid.view import view_config
from pyramid_spine.utils import utcnow

from almanac.models import Event
def begin_day(dt):
    return datetime(dt.year, dt.month, dt.day, 0)

@view_config(route_name='home', renderer='index.html')
def index(request):
    today = begin_day(utcnow())
    #today = Time.zone.now.beginning_of_day
    tomorrow = today + timedelta(days=1)
    #tomorrow = today + 1.day
    after_tomorrow = tomorrow + timedelta(days=1)
    future_cutoff = today + timedelta(weeks=2)
    future_cutoff = today + timedelta(weeks=4)
    events = Event.query.all()
    events = Event.query.filter(Event.start_time.between(today, future_cutoff))

    times_to_events = {
        "today": [],
        "tomorrow": [],
        "later": [],
    }
    #find all events between now and future_cutoff
    for event in events:
        if event.start_time < tomorrow:
            times_to_events['today'].append(event)
        elif event.start_time >= tomorrow and event.start_time < after_tomorrow:
            times_to_events['tomorrow'].append(event)
        else:
            times_to_events['later'].append(event)
    times_to_events['more'] = Event.query.filter(Event.start_time >= future_cutoff).order_by(Event.start_time.asc()).first()
    return times_to_events

