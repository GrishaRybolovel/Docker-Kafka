import json
from kafka import KafkaConsumer
import requests



if __name__ == '__main__':
    # Kafka Consumer
    consumer = KafkaConsumer(
        'messages',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )
    for message in consumer:
        m = json.loads(message.value)
        # Если сообщение корректно, то отправляем ПОСТ запрос на HTML
        if 'абракадабра' in m['message']:
            res = requests.post("http://localhost:3000/api/v1/message_confirmation",
                                {"message_id" : 0, "success" : False})
        else:
            res = requests.post("http://localhost:3000/api/v1/message_confirmation",
                                {"message_id": 0, "success": True})

        print(json.loads(message.value))