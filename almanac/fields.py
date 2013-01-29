from wtforms import widgets, Form
import time
from datetime import datetime
from wtforms.fields.core import _unset_value
from wtforms.validators import DataRequired
from wtforms.fields import (
    FormField,
    DateField,
    Field
)
class TimeField(Field):
    """
    A text field which stores a `datetime.time` matching a format.
    """
    widget = widgets.TextInput()

    def __init__(self, label=None, validators=None, format='%H:%M', **kwargs):
        super(TimeField, self).__init__(label, validators, **kwargs)
        self.format = format

    def _value(self):
        if self.raw_data:
            return ' '.join(self.raw_data)
        else:
            return self.data and self.data.strftime(self.format) or ''

    def process_formdata(self, valuelist):
        if valuelist:
            time_str = ' '.join(valuelist)
            try:
                self.data = time.strptime(time_str, self.format)
            except ValueError:
                self.data = None
                raise ValueError(self.gettext('Not a valid datetime value'))
class Date():
    date = None
    time = None
class SplitDateTimeField(FormField):
    def __init__(self, label=None, validators=None, separator='-', **kwargs):
        FormField.__init__(
            self,
            DateTimeForm,
            label=label,
            validators=validators,
            separator=separator,
            **kwargs
        )

    def process(self, formdata, data=_unset_value):
        if data is _unset_value:
            try:
                data = self.default()
            except TypeError:
                data = self.default
        if data:
            obj = Date()
            obj.date = data.date()
            obj.time = data.time()
        else:
            obj = None
        FormField.process(self, formdata, data=obj)

    def populate_obj(self, obj, name):
        print 'inside'
        if hasattr(obj, name):
            date = self.date.data
            hours, minutes = self.time.data.tm_hour, self.time.data.tm_min
            setattr(obj, name, datetime(date.year, date.month, date.day, hours, minutes))

class DateTimeForm(Form):
    date = DateField(label='', validators=[DataRequired()])
    time = TimeField(label='', validators=[DataRequired()])
