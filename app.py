import process
import logging
import json

from kafka.errors import KafkaError
from time import time
from utils import config
from mq import kafka_consumer

logging.basicConfig(level=logging.INFO)


def main():

    logger.info("Starting legacy host deletion service")

    config.log_config()

    consumer = kafka_consumer.init_consumer()

    while True:
        for data in consumer:
            try:
                print("calling msg_handler()")
                handle_message(json.loads(data.value))
            except Exception:
                logger.exception("An error occurred during message processing")

def handle_message(parsed):
    print("inside msg_handler()")
    print("type(parsed):", type(parsed))
    print("parsed:", parsed)

    insights_id = parsed['insights_id']
    account = parsed['account']
    send_request(insights_id, account)

def send_request(insights_id, account):
    print("sending delete request to legacy")
    

