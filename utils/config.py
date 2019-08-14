import os
import logging

APP_NAME = os.environ.get("APP_NAME", "insights-host-delete")

logger = logging.getLogger(APP_NAME)

def get_namespace():
    try:
        with open("/var/run/secrets/kubernetes.io/serviceaccount/namespace", "r") as f:
            namespace = f.read()
        return namespace
    except EnvironmentError:
        logging.info("Not running in openshift")


def log_config():
    """
    log_config prints out all the config options except for AWS keys
    """
    import sys
    for k, v in sys.modules[__name__].__dict__.items():
        if k == k.upper():
            if "AWS" in k.split("_"):
                continue
            logger.info("Using %s: %s", k, v)

TOPIC = os.environ.get("KAFKA_TOPIC", "platform.inventory.events")
KAFKA_GROUP = os.environ.get("KAFKA_GROUP", "inventory")
BOOTSTRAP_SERVERS = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:29092").split()
LEGACY_URL = "https://access.redhat.com/r/insights/v1/systems"
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
LOG_GROUP = os.environ.get("LOG_GROUP", "platform-dev")


'''
TESTING AUTHENTICATION DATA BASED ON VM
'''
INSIGHTS_ID = '389fb722-1fd1-4a60-bd3e-0f7bb23e0d5b'
ACCOUNT = '540155'
LEGACY_USERNAME = "SomeName"
LEGACY_PASSWORD = "SomePass"
