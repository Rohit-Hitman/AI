from model import tokenizer

# Token Counter + Context Reducer

MAX_TOKENS = 2000  # Set your token limit

def count_tokens(text):
    return len(tokenizer.encode(text))

def reduce_context(history, limit=MAX_TOKENS):
    """Trims history from the beginning if token size is too big."""
    while history and count_tokens(" ".join(history)) > limit:
        history.pop(0)  # remove oldest message
    return history
