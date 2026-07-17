import paho.mqtt.client as mqtt_client

client_id: str = "temp_sensor_publisher"
mqtt_client = mqtt_client.Client(client_id=client_id, userdata=None, protocol=mqtt_client.MQTTv5)


