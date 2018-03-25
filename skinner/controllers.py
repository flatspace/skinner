import logging

from flask import request

log = logging.getLogger(__name__)


def hello_world(message):
    log.info(request.headers)
    # do something
    return 'Hello World. {}'.format(message), 200
