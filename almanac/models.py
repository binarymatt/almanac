from sqlalchemy import (
    Column,
    Integer,
    Text,
    String,
    DateTime,
    ForeignKey,
    Boolean,
    Numeric
)
from sqlalchemy.orm import relationship, backref

from sqlalchemy.ext.declarative import declarative_base, declared_attr

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
class Base(object):
    """Base class which provides automated table name
    and surrogate primary key column.

    """
    @declared_attr
    def __tablename__(cls):
        return '%ss' % cls.__name__.lower()
    id = Column(Integer, primary_key=True)

Base = declarative_base(cls=Base)
Base.query = DBSession.query_property()

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

class Event(Base):
    title = Column(String)
    description = Column(Text)
    start_time = Column(DateTime)
    venue_id = Column(Integer, ForeignKey('venues.id'))
    venue = relationship("Venue", backref=backref('events'))
    url = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    source_id = Column(Integer, ForeignKey('sources.id'), nullable=True)
    #TODO - setup as duplicate
    duplicate_of_id = Column(Integer, nullable=True)
    #duplicates = relationship("Event", backref=backref('canonical', remote_side=[id]))
    end_time = Column(DateTime)
    rrule = Column(String)
    venue_details = Column(Text)

    @property
    def day(self):
        return self.start_time.date()

class Source(Base):
    title = Column(String)
    url = Column(String)
    imported_at = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    reimport = Column(Boolean)

class Venue(Base):
    title = Column(String)
    description = Column(Text)
    address = Column(String)
    url = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    street_address = Column(String)
    locality = Column(String)
    region = Column(String)
    postal_code = Column(String)
    country = Column(String)
    latitude = Column(Numeric(10, 6), nullable=True)
    longitude = Column(Numeric(10, 6), nullable=True)
    email = Column(String)
    telephone = Column(String)
    source_id = Column(Integer)
    duplicate_of_id = Column(Integer)
    closed = Column(Boolean)
    wifi = Column(Boolean)
    access_notes = Column(Text)
    events_count = Column(Integer)

    def __repr__(self):
        return self.title
