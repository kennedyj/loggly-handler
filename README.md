Pyhton Logging Loggly Handler
-----------------------------

[![Build Status](https://travis-ci.org/kennedyj/loggly-handler.png?branch=master)](https://travis-ci.org/kennedyj/loggly-handler) [![Coverage Status](https://coveralls.io/repos/kennedyj/loggly-handler/badge.png?branch=master)](https://coveralls.io/r/kennedyj/loggly-handler?branch=master)

A simple Pyhton logging Loggly handler that can be used to send to a Loggly Gen2 https endpoint. Borrowed the extra fields concept from the graypy logging library.

## Installtion
Download the repository and install the setup.py using the following command
    
    sudo python setup.py install

## Configuration

Excerpt for the json logging configuration.

    {
      "handlers": {
        "loggly": {
          "class": "loggly.handlers.HTTPSHandler",
          "level": "DEBUG",
          "url": "https://logs-01.loggly.com/inputs/TOKEN",
          "facility": "my-app-name"
        }
      }
    }

Adding the handler to a logger

    import logging
    import loggly.handlers
    logger = logging.getLogger(__name__)
    handler = loggly.handlers.HTTPSHandler('https://logs-01.loggly.com/inputs/TOKEN')
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.info('sent to loggly')


Replace
<ul>
<li><strong>TOKEN: </strong>your Loggly Customer Token</li>
</ul>
