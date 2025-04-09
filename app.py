from dotenv import load_dotenv
from agents.search_agent import SearchAgent
from agents.processing_agent import ProcessingAgent
from agents.classification_agent import ClassificationAgent
from agents.summary_agent import SummaryAgent
from agents.synthesis_agent import SynthesisAgent
from agents.audio_agent import AudioAgent

# Load environment variables from .env file
load_dotenv()

def main():
    # Initialize agents
    search_agent = SearchAgent()
    processing_agent = ProcessingAgent()
    classification_agent = ClassificationAgent()
    summary_agent = SummaryAgent()
    synthesis_agent = SynthesisAgent()
    audio_agent = AudioAgent()

    # Example workflow
    query = "machine learning"
    papers = search_agent.search_papers(query)
    summaries = []
    for paper in papers:
        text = processing_agent.extract_text_from_url(paper["link"])
        topic = classification_agent.classify_paper(text, ["AI", "ML", "Data Science"])
        summary = summary_agent.generate_summary(text)
        summaries.append(summary)
    
    synthesis = synthesis_agent.synthesize_findings(summaries)
    audio_agent.generate_audio(synthesis, "output.mp3")

if __name__ == "__main__":
    main()