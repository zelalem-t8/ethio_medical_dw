import pandas as pd
import re
from datetime import datetime

def extract_phone_numbers(text):
    ethiopian_phone_regex = r'(\+251|0)(9|7)\d{8}'
    phones = re.findall(ethiopian_phone_regex, str(text))
    return [''.join(p) for p in phones] if phones else []

def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates(subset=["message", "date", "channel"])
    
    # Extract phone numbers
    df["phone_numbers"] = df["message"].apply(extract_phone_numbers)
    
    # Classify business type
    business_keywords = {
        "hospital": ["hospital", "medical center"],
        "pharmacy": ["pharmacy", "drug store"],
        "clinic": ["clinic", "health center"]
    }
    
    def classify_business(text):
        text = str(text).lower()
        for biz_type, keywords in business_keywords.items():
            if any(kw in text for kw in keywords):
                return biz_type
        return "other"
    
    df["business_type"] = df["message"].apply(classify_business)
    
    # Format dates
    df["date"] = pd.to_datetime(df["date"])
    
    return df

if __name__ == "__main__":
    raw_df = pd.read_csv("data/raw/telegram_messages.csv")
    clean_df = clean_data(raw_df)
    clean_df.to_csv("data/processed/cleaned_messages.csv", index=False)