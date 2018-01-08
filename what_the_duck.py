import logging
from app import app

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.info("in what the duck file")
