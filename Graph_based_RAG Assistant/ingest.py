import os
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from opensearchpy import OpenSearch
from model import embedder

client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    use_ssl=False
)

def load_pdf(path):
    reader = PdfReader(path)
    return "\n".join(page.extract_text() for page in reader.pages)

def ingest():
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    for file in os.listdir("data"):
        if file.endswith(".pdf"):
            text = load_pdf(os.path.join("data", file))
            chunks = splitter.split_text(text)

            for idx, chunk in enumerate(chunks):
                vector = embedder.encode(chunk).tolist()

                doc = {
                    "content": chunk,
                    "embedding": vector
                }

                client.index(
                    index="documents",
                    id=f"{file}-{idx}",
                    body=doc
                )

    print("OpenSearch Ingestion Completed")

if __name__ == "__main__":
    ingest()


