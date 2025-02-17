
import pandas as pd
import joblib
import json
from kafka import KafkaConsumer

# Load model
model = joblib.load('fraud_detection_model.pkl')

# Kafka consumer
consumer = KafkaConsumer(
    'fraud-alerts',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='fraud-consumer-group'
)

for message in consumer:
    transaction = json.loads(message.value)
    df = pd.DataFrame([transaction])
    prediction = model.predict(df)
    print(f"Transaction: {transaction} | Fraud Prediction: {'Fraud' if prediction[0] == 1 else 'Legit'}")
