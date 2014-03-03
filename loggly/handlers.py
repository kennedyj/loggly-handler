import logging
import logging.handlers

import socket
import traceback

from requests_futures.sessions import FuturesSession

session = FuturesSession()


def bg_cb(sess, resp):
    """ Don't do anything with the response """
    pass


class HTTPSHandler(logging.Handler):
    def __init__(self, url, fqdn=False, localname=None, facility=None):
        logging.Handler.__init__(self)
        self.url = url
        self.fqdn = fqdn
        self.localname = localname
        self.facility = facility

    def get_full_message(self, record):
        if record.exc_info:
            return '\n'.join(traceback.format_exception(*record.exc_info))
        else:
            return record.getMessage()

    def to_loggly(self, record):
        if self.fqdn:
            host = socket.getfqdn()
        elif self.localname:
            host = self.localname
        else:
            host = socket.gethostname()

        return {
            'host': host,
            'message': record.getMessage(),
            'full_message': self.get_full_message(record),
            'timestamp': record.created,
            'level': logging.getLevelName(record.levelno),
            'facility': self.facility or record.name,
        }

    def emit(self, record):
        try:
            payload = self.to_loggly(record)
            session.post(self.url, data=payload, background_callback=bg_cb)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)
