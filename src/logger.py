"""
logger.py

This module defines loggers with different settings/configurations that can be chosen automatically based on the ENVIRONMENT variable.
"""

import logging
import logging.config
import os
import sys

# Define base log configuration
base_log_config: dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple_formatter": {
            "format": "%(name)-8s %(asctime)s - %(levelname)s - %(message)s",
            # Leaving datefmt string empty will result in the following timeformat:
            # 2023-08-24 13:45:42,774
            # TODO: Explicit formatting would be better such as
            # "datefmt": "%Y-%m-%d %H:%M:%S"
            # However, with datefmt it's apparently not possible to add milliseconds to
            # the time. Thus, using empty string for now.
            "datefmt": "",
        },
        "detailed_formatter": {
            "format": " %(name)-8s[%(asctime)s  %(filename)s -> %(funcName)s(): line:%(lineno)s] %(levelname)s: %(message)s"
        },
    },
    # Define handlers than can be used in loggers
    "handlers": {
        "stream_handler": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple_formatter",
            "stream": sys.stderr,
        },
        "local_docker_handler": {
            "class": "logging.handlers.SysLogHandler",
            "level": "DEBUG",
            "formatter": "detailed_formatter",
            "address": ("log_server", 5237),
        },
    },
    # Under "loggers", every dict is a configuration for a specific logger(key[logger name]-value[config])
    "loggers": {
        "local_logger": {
            "handlers": ["local_docker_handler"],
            "level": "DEBUG",
            "propagate": True,  # If true, this logger would have its own handler and root’s handler
        }
    },
    # Root logger configuration
    "root": {
        "handlers": ["stream_handler"],
        "level": "WARNING",
        "propagate": False,
    },
}

# Set configuration
logging.config.dictConfig(base_log_config)


# Get logger based on environment
if os.environ.get("ENVIRONMENT") == "local":
    logger = logging.getLogger("local_logger")
else:
    logger = logging.getLogger()
