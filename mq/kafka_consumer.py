import json

from kafka import KafkaConsumer
from utils import config


def init_consumer():
    consumer = KafkaConsumer(config.TOPIC,
                             group_id=config.KAFKA_GROUP,
                             bootstrap_servers=config.BOOTSTRAP_SERVERS,
                             value_deserializer=lambda m: json.loads(m.decode("utf-8"))
                             )

    return consumer
