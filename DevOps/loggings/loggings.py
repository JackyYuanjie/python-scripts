#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import logging.handlers
import datetime

# logger = logging.getLogger('/var/log/syslog')
# logger.setLevel(logging.error)
#
# handlers = logging.FileHandler('error.log')
# handlers .setLevel(logging.ERROR)
# handlers.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
#
# logger.addHandler(handlers)
#
# logger.error('error message')

"""
logging.debug("This is a debug log")
logging.info("This is a info log")
logging.warning("This is a warning log")
logging.error("This is a error log")
logging.critical("This is a critical log")

logging.log(logging.DEBUG,"This is a debug log")
logging.log(logging.INFO,"info")
logging.log(logging.WARNING,'warning')
logging.log(logging.ERROR,"error")
logging.log(logging.CRITICAL,"critical")

"""

import logging
logging.basicConfig(level=logging.ERROR,format= '%(asc')



