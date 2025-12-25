
from model import llm
from utils import count_tokens, MAX_TOKENS

# Local Conversation Memory + Summarizer

def summarize(history):
    text = "\n".join(history)
    prompt = f"Summarize this conversation briefly:\n{text}\nSummary:"
    return llm(prompt)

class MemoryManager:
    def __init__(self, max_tokens=MAX_TOKENS):
        self.max_tokens = max_tokens
        self.history = []

    def add(self, user_msg, assistant_msg=None):
        self.history.append(f"User: {user_msg}")
        if assistant_msg:
            self.history.append(f"Assistant: {assistant_msg}")

        # If memory too large, replace history with summary
        if count_tokens("\n".join(self.history)) > self.max_tokens:
            summary = summarize(self.history)
            self.history = [f"[Summary so far]: {summary}"]

    def get(self):
        return "\n".join(self.history)

