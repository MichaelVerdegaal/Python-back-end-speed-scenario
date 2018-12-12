from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
from waitress import serve
from util import *
from loop_util import *


@view_config(route_name='api.loop', renderer='json')
def data(request):
    """Handle the request to convert the street_name to lowercase"""
    data = load_data()
    response = simple_for_loop(data)
    # response = for_loop_no_dots(data)
    # response = list_comprehension(data)
    # response = list_comprehension_no_dots(data)
    # response = generator_expression(data)
    return Response(response)


if __name__ == '__main__':
    config = Configurator()
    config.include('pyramid_debugtoolbar')

    config.add_route('api.loop', '/loop')

    config.scan()
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=1212)
