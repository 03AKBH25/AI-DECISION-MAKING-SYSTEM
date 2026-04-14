from app.rag.vector_store import search
from app.services.llm_service import generate_response
from app.services.redis_service import add_message, get_messages

def analyze_text(text: str, user_id: str):
    # Store message in Redis
    add_message(user_id, text)

    # Get conversation history
    history = get_messages(user_id)

    # Combine context
    conversation_context = " ".join(history)

    # RAG search
    results = search(conversation_context)
    retrieved_context = " ".join([item["rule"] for item in results])

    # LLM
    llm_output = generate_response(conversation_context, retrieved_context)

    return {
        "history": history,
        "response": llm_output
    }