
from langgraph.graph import StateGraph, END
from opensearchpy import OpenSearch
from model import llm, embedder
from utils import reduce_context
from memory import MemoryManager

memory = MemoryManager()

# LangGraph with retrieval + memory + token management

client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    use_ssl=False
)

class State:
    question: str
    retrieved: list
    history: list
    answer: str


def retrieve(state):
    # vector embedding search
    q_emb = embedder.encode(state["question"]).tolist()
    result = client.search(
        index="documents",
        size=3,
        body={
            "query": {
                "knn": {
                    "embedding": {
                        "vector": q_emb,
                        "k": 3
                    }
                }
            }
        }
    )
    docs = [hit["_source"]["content"] for hit in result["hits"]["hits"]]
    state["retrieved"] = docs
    return state


def formulate_prompt(state):
    history = memory.get()
    context_docs = "\n".join(state["retrieved"])

    # Build prompt
    prompt = f"""
### Conversation History:
{history}

### Relevant Knowledge:
{context_docs}

### User Question:
{state['question']}

### Answer:
    """

    # Token management
    prompt_tokens = len(prompt.split())
    if prompt_tokens > 2000:
        history = reduce_context(history.split("\n"))
        memory.history = history
    return prompt


def generate_answer(state):
    prompt = formulate_prompt(state)
    answer = llm(prompt)
    state["answer"] = answer

    # Add to memory
    memory.add(state["question"], answer)
    return state


# 🔥 Build graph
graph = StateGraph(State)
graph.add_node("retrieve", retrieve)
graph.add_node("answer", generate_answer)

graph.set_entry_point("retrieve")
graph.add_edge("retrieve", "answer")
graph.add_edge("answer", END)

app = graph.compile()


