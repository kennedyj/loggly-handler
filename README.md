Python Logging Loggly Handler
-----------------------------

[![Build Status](https://travis-ci.org/kennedyj/loggly-handler.png?branch=master)](https://travis-ci.org/kennedyj/loggly-handler) [![Coverage Status](https://coveralls.io/repos/kennedyj/loggly-handler/badge.png?branch=master)](https://coveralls.io/r/kennedyj/loggly-handler?branch=master)

A simple Python logging Loggly handler that can be used to send to a Loggly Gen2 https endpoint. Borrowed the extra fields concept from the graypy logging library.

## Installation
Download the repository using pip 
    
    sudo pip install loggly-handler

## Configuration

Create a Configuration file python.conf and add HTTPSHandler to Configuration File.
    [handlers]
    keys=HTTPSHandler
    
    [handler_HTTPSHandler]
    class=loggly.handlers.HTTPSHandler
    level=INFO
    args=('https://logs-01.loggly.com/inputs/TOKEN/tag/python','POST')
    
    [formatters]
    keys=
    
    [loggers]
    keys=root
    
    [logger_root]
    handlers=HTTPSHandler

## Use Configuration in python file

    import logging
    import logging.config
    import loggly.handlers
    
    logging.config.fileConfig('python.conf')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.info('test Loggly log')


Replace
<ul>
<li><strong>TOKEN: </strong>your Loggly Customer Token</li>
</ul>
