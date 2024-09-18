import pandas as pd
from src.sentiment_analysis.py import analyze_sentiment # type: ignore
from src.utils import logger

def clean_text(text):
    # Add text cleaning steps here
    return text

def process_customer_support_data(file_path):
    try:
        data = pd.read_csv(file_path)
        data['support_interaction'] = data['support_interaction'].apply(clean_text)
        
        sentiments = []
        for index, row in data.iterrows():
            sentiment = analyze_sentiment(row['support_interaction'])
            sentiments.append(sentiment)
        
        data['sentiment'] = sentiments
        processed_file_path = file_path.replace('.csv', '_processed.csv')
        data.to_csv(processed_file_path, index=False)
        logger.info(f"Processed data saved to {processed_file_path}")
        return processed_file_path
    except Exception as e:
        logger.error(f"Error in processing data: {e}")
        return None
