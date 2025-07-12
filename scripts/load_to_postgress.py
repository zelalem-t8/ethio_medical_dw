import pandas as pd
from sqlalchemy import create_engine

# Database connection
engine = create_engine('postgresql://postgres:root@localhost/medical')

# Load and clean messages
messages = pd.read_csv('data/processed/cleaned_messages.csv')
messages['date'] = pd.to_datetime(messages['date'])
messages.to_sql('raw_telegram_messages', engine, if_exists='replace', index=False)

# Load detections
detections = pd.read_csv('data/processed/object_detections.csv')
detections.to_sql('raw_object_detections', engine, if_exists='replace', index=False)

print("Data successfully loaded to PostgreSQL!")