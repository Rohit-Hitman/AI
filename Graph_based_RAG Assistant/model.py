from langchain_community.llms import Ollama
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer

# Add tokenizer for token counting.

llm = Ollama(model="llama3")

# Embeddings
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Tokenizer for token management
tokenizer = AutoTokenizer.from_pretrained("hf-internal-testing/llama-tokenizer")
