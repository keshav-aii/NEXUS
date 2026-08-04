import logging
import os


LOG_FOLDER = "logs"

LOG_FILE = os.path.join(
    LOG_FOLDER,
    "nexus.log"
)


os.makedirs(
    LOG_FOLDER,
    exist_ok=True
)


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def info(message):

    logging.info(
        message
    )


def error(message):

    logging.error(
        message
    )