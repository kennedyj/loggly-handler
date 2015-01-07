Python Logging Loggly Handler
-----------------------------

[![Build Status](https://travis-ci.org/kennedyj/loggly-handler.png?branch=master)](https://travis-ci.org/kennedyj/loggly-handler) [![Coverage Status](https://coveralls.io/repos/kennedyj/loggly-handler/badge.png?branch=master)](https://coveralls.io/r/kennedyj/loggly-handler?branch=master)

A simple Pyhton logging Loggly handler that can be used to send to a Loggly gen 1 https endpoint. Borrowed the extra fields concept from the graypy logging library.

## Configuration

Replace ``MY-INPUT`` with your API-token).

Excerpt for the json logging configuration.

    {
      "handlers": {
        "loggly": {
          "class": "loggly.handlers.HTTPSHandler",
          "level": "INFO",
          "url": "https://logs-01.loggly.com/inputs/MY-INPUT",
          "facility": "my-app-name"
        }
      }
    }

Adding the handler to a logger

    logger = logging.getLogger(__name__)
    handler = loggly.handlers.HTTPSHandler('https://logs-01.loggly.com/inputs/MY-INPUT')
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    logger.info('sent to loggly')
