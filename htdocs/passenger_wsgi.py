import os
import sys
import imp


sys.path.insert(0, os.path.dirname(__file__))

wsgi = imp.load_source('wsgi', 'htdocs/wsgi.py')
application = wsgi.application

"""
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    message = 'It works! inside save folder\n'
    version = 'Python %s\n' % sys.version.split()[0]
    response = '\n'.join([message, version])
    return [response.encode()]
"""