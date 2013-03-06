from wtforms import Form, TextField, validators, TextAreaField

from almanac.fields import SplitDateTimeField
class EventForm(Form):
    name = TextField('Event Name', [validators.Required()])
    venue = TextField('Venue', [validators.Required()])
    #start_time = DateTimeField('start time', [validators.Required()])
    start_time = SplitDateTimeField('start time')
    end_time = SplitDateTimeField('end time')
    website = TextField('website', [])
    description = TextAreaField('description', [])
    venue_details = TextAreaField('venue details')

