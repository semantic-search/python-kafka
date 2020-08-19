from kafka import KafkaProducer
import json

TOPIC_NAME = "maintopic"

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda x: json.dumps(x).encode("utf-8"),
)

future = producer.send(TOPIC_NAME, value="Some message to kafka topic")
result = future.get(timeout=60)
print(result)
