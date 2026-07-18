import logging
from logging import Logger

import paho.mqtt.client as mqtt_client

log: Logger = logging.getLogger(__name__)
log.setLevel(logging.INFO)

client_id: str = "temp_sensor_publisher"
mqtt_client = mqtt_client.Client(client_id=client_id, userdata=None, protocol=mqtt_client.MQTTv5)
mqtt_client.username_pw_set(username='hivemq.webclient.1784364514410', password='L3ESGMP27b4jTOwAjDsqcdP@RIa&aE$8')
mqtt_client.connect(host='728a07137f2247df9daa56dcd266f454.s1.eu.hivemq.cloud', port=8883)


def publish_room_temp() -> None:
    print("Publishing zimmer temp")
    mqtt_client.publish(topic='zimmer_temp', payload="23", qos=1)

def main():
    print("MQTT Publisher started successfully")

if __name__ == '__main__':
    publish_room_temp()
