from PyPDF2 import PdfReader
import requests

class ProcessingAgent:
    def extract_text_from_pdf(self, file_path):
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

    def extract_text_from_url(self, url):
        response = requests.get(url)
        return response.text