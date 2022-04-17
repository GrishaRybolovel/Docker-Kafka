import time
import json
import random
from datetime import datetime
from kafka import KafkaProducer
import requests


# Messages will be serialized as JSON
def serializer(message):
    return json.dumps(message).encode('utf-8')


# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

if __name__ == '__main__':
    # Infinite loop - runs until you kill the program
    while True:
        # Generate a message
        message = requests.get("http://localhost:3000/api/v1/message/")
        if message is not None:
            # Send it to our 'messages' topic
            print(f'Producing message @ {datetime.now()} | Message = {str(message)}')
            producer.send('messages', message)

            # Sleep for a random number of seconds
            #time_to_sleep = random.randint(1, 11)
            #time.sleep(time_to_sleep)