Pyhton Logging Loggly Handler
-----------------------------

A simple Pyhton logging Loggly handler that can be used to send to a Loggly gen 1 https endpoint. Borrowed the extra fields concept from the graypy logging library.

## Configuration

Excerpt for the json logging configuration.

    {
      "handlers": {
        "loggly": {
          "class": "loggly.handlers.HTTPSHandler",
          "level": "INFO",
          "url": "https://logs.loggly.com/inputs/MY-INPUT",
          "facility": "my-app-name"
        }
      }
    }

Adding the handler to a logger

    logger = logging.getLogger(__name__)
    handler = loggly.handlers.HTTPSHandler('https://logs.loggly.com/inputs/MY-INPUT')
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    logger.info('sent to loggly')
