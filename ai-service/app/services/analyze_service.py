from app.rag.vector_store import search
from app.services.llm_service import generate_response

#memory
conversation_memory = []

def analyze_text(text: str):
    #Store current message
    conversation_memory.append(text)

    #Keep only last 5 messages
    recent_context = conversation_memory[-5:]

    #Combine into context string
    conversation_context = " ".join(recent_context)

    #RAG search using full context