import os

logging.basicConfig(level=logging.INFO)

def get_namespace():
    try:
        with open("/var/run/secrets/kubernetes.io/serviceaccount/namespace", "r") as f:
            namespace = f.read()
        return namespace
    except EnvironmentError:
        logger.info("Not running in openshift")

TOPIC = os.environ.get("KAFKA_TOPIC", "platform.inventory.host-egress")
KAFKA_GROUP = os.environ.get("KAFKA_GROUP", "inventory-mq")
BOOTSTRAP_SERVERS = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "kafka:29092")