from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
from waitress import serve
from util import load_data, total_slow, total_fast
from loop_util import *
from format_util import *
from concat_util import *
# import json
# import simplejson as json
import ujson as json


@view_config(route_name='api.loop', renderer='json')
def loop(request):
    """Handle the request to convert the street_name to lowercase"""
    data = load_data()
    response = simple_for_loop(data)
    # response = for_loop_no_dots(data)
    # response = list_comprehension(data)
    # response = list_comprehension_no_dots(data)
    # response = generator_expression(data)
    return Response(json.dumps(response))


@view_config(route_name='api.format', renderer='json')
def loop(request):
    """Handle the request to format the house numbers"""
    data = load_data()
    # response = format_percentage(data)
    response = format_dot_format(data)
    # response = format_f_string(data)
    return Response(json.dumps(response))


@view_config(route_name='api.concat', renderer='json')
def concat(request):
    """Handle the request to format the house numbers"""
    data = load_data()
    # response = concat_plus(data)
    # response = concat_plus_is(data)
    response = concat_join(data)
    return Response(json.dumps(response))


@view_config(route_name='api.slow', renderer='json')
def slow(request):
    """Handle the request to format the house numbers"""
    data = load_data()
    response = total_slow(data)
    return Response(json.dumps(response))


@view_config(route_name='api.fast', renderer='json')
def fast(request):
    """Handle the request to format the house numbers"""
    data = load_data()
    response = total_fast(data)
    return Response(json.dumps(response))


if __name__ == '__main__':
    config = Configurator()
    config.include('pyramid_debugtoolbar')

    config.add_route('api.loop', '/loop')
    config.add_route('api.format', '/format')
    config.add_route('api.concat', '/concat')
    config.add_route('api.slow', '/slow')
    config.add_route('api.fast', '/fast')

    config.scan()
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=1212)
