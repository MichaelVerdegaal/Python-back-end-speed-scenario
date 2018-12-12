from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
from waitress import serve
from util import *


@view_config(route_name='api.data', renderer='json')
def data(request):
    """Handle the request, to retrieve the entire dataset"""
    data = load_features()
    return Response(data)


if __name__ == '__main__':
    config = Configurator()
    config.include('pyramid_debugtoolbar')

    config.add_route('api.home', '/')
    config.add_route('api.data', '/data')

    config.scan()
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=1212)
