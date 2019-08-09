import json
import logging
import os

from kafka import KafkaConsumer
from utils import config



def init_consumer():
    consumer = KafkaConsumer(config.TOPIC, group_id=config.KAFKA_GROUP, 
    bootstrap_servers=config.BOOTSTRAP_SERVERS)

    return consumer