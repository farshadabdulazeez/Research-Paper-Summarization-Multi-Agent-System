from dotenv import load_dotenv
import os
from groq import Groq

# Load environment variables from .env file
load_dotenv()

class SynthesisAgent:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY is not set in the .env file.")
        self.client = Groq(api_key=api_key)

    def synthesize_findings(self, summaries):
        prompt = f"Synthesize the following summaries into a cohesive narrative:\n\n{summaries}"
        response = self.client.chat.completions.create(
            model="llama3-70b-8192",  
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200  # Adjust max_tokens to control output length
        )
        return response.choices[0].message.content.strip()