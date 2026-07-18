import logging
from logging import Logger

import paho.mqtt.client as mqtt_client
from paho import mqtt
from paho.mqtt.client import Client, MQTTMessageInfo

log: Logger = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class MqttPublisher:
    def __init__(self):
        self.client_id: str = 'temp_sensor_publisher'
        self.host: str = '728a07137f2247df9daa56dcd266f454.s1.eu.hivemq.cloud'
        self.port: int = 8883
        self.username: str = 'hivemq.webclient.1784364514410'
        self.password: str = 'L3ESGMP27b4jTOwAjDsqcdP@RIa&aE$8'
        self.client: Client = None

    def init_mqtt_client(self) -> Client:
        try:
            self.client = mqtt_client.Client(client_id=self.client_id, userdata=None, protocol=mqtt_client.MQTTv5)
            self.client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
            self.client.username_pw_set(username=self.username, password=self.password)
            self.client.connect(host=self.host, port=self.port)

            # Start background network loop thread
            self.client.loop_start()

            return self.client
        except Exception as e:
            print(f"Connection error: {e}")
        return None

    def publish_room_temp(self) -> None:
        message_info: MQTTMessageInfo = self.client.publish(topic='zimmer_temp', payload="23", qos=1)
        message_info.wait_for_publish(timeout=5)
        print(f'Published message to Message Broker: {message_info.is_published()}')

    def disconnet(self):
        self.client.disconnect()
        self.client.loop_stop()

def main():
    print("MQTT Publisher started successfully")
    publisher: MqttPublisher = MqttPublisher()
    publisher.init_mqtt_client()
    publisher.publish_room_temp()


if __name__ == '__main__':
    main()
