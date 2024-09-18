# GPT Sentiment Analysis Pipeline

## Description
This project creates a sentiment analysis pipeline using OpenAI's GPT model to analyze customer support interactions.

## Setup

1. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2. Install required libraries:
    ```bash
    pip install openai pandas numpy nltk
    ```

3. Configure the OpenAI API key in `config/config.py`.

## Usage

1. Place your customer support data CSV file in the `data` directory.

2. Run the main script:
    ```bash
    python main.py data/customer_support_data.csv
    ```

## Testing

Run the unit tests:
```bash
python -m unittest discover -s tests
