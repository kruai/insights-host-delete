import logging
import json
import requests

from kafka.errors import KafkaError
from requests.auth import HTTPBasicAuth
from time import time
from utils import config
from mq import kafka_consumer


logger = logging.getLogger(config.APP_NAME)

logger.info("Starting legacy host deletion service")
config.log_config()

consumer = kafka_consumer.init_consumer()

def handle_message(parsed):

    try:
        send_request(parsed["rhel_machine_id"], parsed["account"])
    except KeyError as e:
        logger.exception("Missing Key in Message: %s", e)


def send_request(rhel_machine_id, account):
    logger.debug("sending delete request to legacy")
    URL = "{0}/{1}?account_number={2}".format(config.LEGACY_URL, rhel_machine_id, account)
    r = requests.delete(URL, auth=HTTPBasicAuth(config.LEGACY_USERNAME, config.LEGACY_PASSWORD))
    logger.debug(r.text)

for data in consumer:
    handle_message(data.value)
