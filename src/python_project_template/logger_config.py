import sys

# Define base log configuration
base_log_config: dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple_formatter": {
            "format": "%(name)-8s %(asctime)s - %(message)s",
            # Leaving datefmt string empty will result in the following timeformat:
            # 2023-08-24 13:45:42,774
            "datefmt": "",
        },
        "detailed_formatter": {
            "format": " %(name)-8s %(levelname)s: [%(asctime)s,%(msecs)03d  %(filename)s -> %(funcName)s(): line:%(lineno)s] - %(message)s",
            "datefmt": "%Y-%m-%d,%H:%M:%S",
        },
    },
    # Define handlers than can be used in loggers
    "handlers": {
        "stream_handler": {
            "class": "logging.StreamHandler",
            "formatter": "detailed_formatter",
            "stream": sys.stdout,
        },
    },
    # Root logger configuration
    "root": {
        "handlers": ["stream_handler"],
        "level": "INFO",
        "propagate": False,
    },
    "loggers": {
    },
}

# import logging
# import logging.config

# Setup logger for this module
# logging.config.dictConfig(base_log_config)
# logger = logging.getLogger(__name__)
