# from dotenv import load_dotenv
# import os
# from groq import Groq

# # Load environment variables from .env file
# load_dotenv()

# class ClassificationAgent:
#     def __init__(self):
#         api_key = os.getenv("GROQ_API_KEY")
#         if not api_key:
#             raise ValueError("GROQ_API_KEY is not set in the .env file.")
#         self.client = Groq(api_key=api_key)

#     def classify_paper(self, text, topics):
#         # Truncate the input text to avoid exceeding token limits
#         max_input_length = 5000  # Adjust based on your token limit
#         truncated_text = text[:max_input_length]

#         prompt = f"Classify the following text into one of these topics: {', '.join(topics)}\n\nText: {truncated_text}"
#         response = self.client.chat.completions.create(
#             model="llama3-70b-8192",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": prompt}
#             ],
#             max_tokens=50  # Control the output length
#         )
#         return response.choices[0].message.content.strip()


from dotenv import load_dotenv
import os
from groq import Groq
import tiktoken

# Load environment variables from .env file
load_dotenv()

class ClassificationAgent:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY is not set in the .env file.")
        self.client = Groq(api_key=api_key)

    def truncate_text(self, text, max_tokens):
        # Use tiktoken to count tokens and truncate the text
        encoding = tiktoken.get_encoding("cl100k_base")  # Encoding used by many models
        tokens = encoding.encode(text)
        truncated_tokens = tokens[:max_tokens]
        return encoding.decode(truncated_tokens)

    def classify_paper(self, text, topics):
        # Truncate the input text to avoid exceeding token limits
        max_tokens = 4000  # Adjust based on your token limit
        truncated_text = self.truncate_text(text, max_tokens)

        prompt = f"Classify the following text into one of these topics: {', '.join(topics)}\n\nText: {truncated_text}"
        response = self.client.chat.completions.create(
            model="llama3-70b-8192",  # Replace with the Groq model you want to use
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50  # Control the output length
        )
        return response.choices[0].message.content.strip()