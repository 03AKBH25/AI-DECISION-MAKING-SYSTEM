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
    results = search(conversation_context)

    retrieved_context  =" ".join([item["rule"] for item in results])

    #Send both current input and conversation context to LLM

    llm_output = generate_response(conversation_context, retrieved_context)

    return {
        "memory": recent_context,
        "response": llm_output
    }