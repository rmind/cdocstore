#
# Copyright (c) 2020 Nox Technologies Ltd <info at noxt eu>
# All rights reserved.
#
# Use is subject to license terms, as specified in the LICENSE file.
#

from os import getenv
from flask.app import Flask
from flask import Blueprint
from flask_restplus import Api

from core.document import api as document_ns


def _http_no_cache(r):
    r.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    r.headers['Pragma'] = 'no-cache'
    r.headers['Expires'] = '0'
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


def create_app(api, blueprint) -> Flask:
    app = Flask(__name__, static_url_path='/static')
    app.debug = getenv("APP_DEBUG", False)
    app.after_request(_http_no_cache)
    app.register_blueprint(blueprint, url_prefix='/api/v1')
    return app


blueprint = Blueprint('api', __name__)
api = Api(blueprint, title='CDocStore', version='1.0')
api.add_namespace(document_ns)
app = create_app(api, blueprint)


@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)


@app.route("/")
def index_html():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run()
