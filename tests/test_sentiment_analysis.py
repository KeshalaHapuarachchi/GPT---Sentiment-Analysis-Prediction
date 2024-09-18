import unittest
from src.sentiment_analysis import analyze_sentiment

class TestSentimentAnalysis(unittest.TestCase):
    
    def test_analyze_sentiment(self):
        test_text = "I am happy with the service."
        result = analyze_sentiment(test_text)
        self.assertNotEqual(result, "Error")
        self.assertTrue("positive" in result.lower() or "negative" in result.lower() or "neutral" in result.lower())

if __name__ == "__main__":
    unittest.main()
