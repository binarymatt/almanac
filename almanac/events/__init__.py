def includeme(config):
    config.add_route('event.list', '')
    config.add_route('events.ics', 'events.ics')
    config.add_route('event.add', '/add')
    config.add_route('event.new', '/new')
    config.add_route('event.detail', '/{id}')
    #config.scan()
