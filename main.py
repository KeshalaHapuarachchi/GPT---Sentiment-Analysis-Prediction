import sys
from src.data_processing import process_customer_support_data
from src.utils import logger

def main(file_path):
    logger.info("Starting sentiment analysis pipeline...")
    processed_file_path = process_customer_support_data(file_path)
    if processed_file_path:
        logger.info(f"Sentiment analysis completed. Processed data saved at {processed_file_path}")
    else:
        logger.error("Sentiment analysis failed.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_customer_support_data_csv>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    main(file_path)
