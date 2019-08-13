import os
import logging

logging.basicConfig(level=logging.INFO)

def get_namespace():
    try:
        with open("/var/run/secrets/kubernetes.io/serviceaccount/namespace", "r") as f:
            namespace = f.read()
        return namespace
    except EnvironmentError:
        logging.info("Not running in openshift")

TOPIC = os.environ.get("KAFKA_TOPIC", "platform.inventory.events")
KAFKA_GROUP = os.environ.get("KAFKA_GROUP", "inventory")
BOOTSTRAP_SERVERS = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:29092")
LEGACY_URL = "https://access.redhat.com/r/insights/v1/systems"


'''
TESTING AUTHENTICATION DATA BASED ON VM
'''
USERNAME = "rhn-support-alcohan"
PASSWORD = "Qg@8dN91pFyAED%bxO"
INSIGHTS_ID = '389fb722-1fd1-4a60-bd3e-0f7bb23e0d5b'
ACCOUNT = '540155'