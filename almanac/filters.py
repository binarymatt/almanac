import json
from jinja2 import Markup

def datestamp(item):
    stamp = "This item was %s"
    if item.source is None:
        stamp = stamp % " added directly to nashvl cal"
    else:
        stamp = stamp % "imported from %s" % item.source.title
    stamp = stamp + " <strong>%s</strong>" % item.created_at.strftime("%A, %B %d, %Y at %I:%M%p")
    return Markup(stamp)

def htmlsafe_dumps(item):
    """Works exactly like :func:`dumps` but is safe for use in ``<script>``
    tags.  It accepts the same arguments and returns a JSON string.  Note that
    this is available in templates through the ``|tojson`` filter but it will
    have to be wrapped in ``|safe`` unless **true** XHTML is being used.
    """
    rv = json.dumps(item)
    rv = rv.replace('/', '\\/')
    return rv.replace('<!', '<\\u0021')
