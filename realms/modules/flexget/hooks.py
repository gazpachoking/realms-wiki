from flask import g


def before_request():
    g.assets['css'].append('flexget.css')
