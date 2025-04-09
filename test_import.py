from dotenv import load_dotenv
import os
from agents.classification_agent import ClassificationAgent

# Load environment variables from .env file
load_dotenv()

def test_classification_agent():
    classification_agent = ClassificationAgent()
    # Simulate a large input text
    sample_text = "Machine learning is a field of artificial intelligence that uses algorithms to learn from data. " * 500
    topics = ["AI", "ML", "Data Science"]
    try:
        topic = classification_agent.classify_paper(sample_text, topics)
        print(f"Classified text into topic: {topic}")
    except Exception as e:
        print(f"Classification Agent failed with error: {e}")

if __name__ == "__main__":
    test_classification_agent()