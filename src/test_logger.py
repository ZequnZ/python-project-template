import logging

from logger import logger

root_logger = logging.getLogger()

logger.info("test")
root_logger.warning("test")
