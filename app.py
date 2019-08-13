import logging
import json
import requests

from kafka.errors import KafkaError
from requests.auth import HTTPBasicAuth
from time import time
from utils import config
from mq import kafka_consumer


logging.info("Starting legacy host deletion service")

consumer = kafka_consumer.init_consumer()

def handle_message(parsed):
    print("inside msg_handler()")
    print("type(parsed):", type(parsed))
    print("parsed:", parsed)

    insights_id = parsed['insights_id']
    account = parsed['account']

    if insights_id or account is None:
        print("insights_id not defined, cannot send request to legacy")
    else:
        send_request(insights_id, account)


def send_request(insights_id, account):
    print("sending delete request to legacy")
    URL = config.LEGACY_URL + '/' + insights_id + '?' + 'account_number=' + account
    r = requests.delete(URL, auth = HTTPBasicAuth(config.USERNAME,config.PASSWORD))
    print(r.text)

for data in consumer:
    print("calling msg_handler()")
    handle_message(json.loads(data.value))