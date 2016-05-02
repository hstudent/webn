import urllib

def app(environ, start_response):
    """Simplest possible application object"""
    #data = 'Hello, World! Version 2\n'
    #qs = environ['QUERY_STRING']
    qs = urllib.unquote(environ['QUERY_STRING'])
    #print(qs)
    qps = qs.split("&")
    data = "\n".join(qps)
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])

