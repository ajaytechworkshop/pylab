class MqttSubscriber:
    def __init__(self):
        self.topic = "zimmer_temp"


def main():
    subscriber: MqttSubscriber = MqttSubscriber()
    print(f'Subscribed to {subscriber.topic}')
