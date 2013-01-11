from jinja2 import Markup

def datestamp(item):
    stamp = "This item was %s"
    if item.source is None:
        stamp = stamp % " added directly to nashvl cal"
    else:
        stamp = stamp % "imported from %s" % item.source.title
    stamp = stamp + " <strong>%s</strong>" % item.created_at.strftime("%A, %B %d, %Y at %I:%M%p")
    return Markup(stamp)
