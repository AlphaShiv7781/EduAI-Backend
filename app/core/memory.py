from collections import defaultdict

# In-memory chat storage
chat_memory = defaultdict(list)

def get_history(session_id: str):
    return chat_memory[session_id]

def add_message(session_id: str, role: str, content: str):
    chat_memory[session_id].append({
        "role": role,
        "content": content
    })
