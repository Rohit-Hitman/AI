
from fastapi import FastAPI
from graph import app as graph_app

api = FastAPI()

@api.get("/ask")
def ask(q: str):
    res = graph_app.invoke({"question": q})
    return {"answer": res["answer"]}


