from . import web

@web.route('/hello/<name>')
def hello(name):
    return 'hello, %s' % name