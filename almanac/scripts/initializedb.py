import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from almanac.models import initialize_sql, DBSession, Event, Venue, Source
import pytz
current = pytz.timezone('US/Central')
utc = utc = pytz.utc
fields = ['start_time', 'end_time', 'created_at','updated_at']
def normalize_model(m):
    for f in fields:
        i = getattr(m, f, None)
        if i:
            i = i.replace(tzinfo=current)
            i = i.astimezone(utc)
            if hasattr(utc, 'normalize'):
                # available for pytz time zones
                i = utc.normalize(i)
            i = i.replace(tzinfo=None)
            setattr(m, f, i)
    return m
def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd)) 
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    session = DBSession()
    #DBSession.configure(bind=engine)
    #Base.metadata.create_all(engine)
    with transaction.manager:
        for event in Event.query.all():
            m = normalize_model(event)
            session.add(m)
    #    model = MyModel(name='one', value=1)
    #    DBSession.add(model)
