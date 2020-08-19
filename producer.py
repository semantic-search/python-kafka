from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda x: json.dumps(x).encode("utf-8"),
)

future = producer.send("my_topic", value="Some message from kafka id")
result = future.get(timeout=60)
print(result)
