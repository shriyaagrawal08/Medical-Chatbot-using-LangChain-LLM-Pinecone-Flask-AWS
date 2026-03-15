from flask import Flask, render_template, request
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFaceHub
from langchain.chains import RetrievalQA
import os


from dotenv import load_dotenv
load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

app = Flask(__name__)


# -----------------------------
# Load Embedding Model
# -----------------------------
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------
# Load FAISS Vector Database
# -----------------------------
vectorstore = FAISS.load_local(
    "faiss_index",
    embedding_model,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 2}
)

# -----------------------------
# Load Phi3 model via Ollama
# -----------------------------

llm = HuggingFaceHub(
    repo_id="google/flan-t5-base",
    huggingfacehub_api_token=hf_token,
    model_kwargs={"temperature": 0.2, "max_length": 128}
)

# -----------------------------
# Create RAG chain
# -----------------------------
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff"
)

# -----------------------------
# Flask Routes
# -----------------------------

@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["POST"])
def chat():

    msg = request.form["msg"]

    response = qa_chain.invoke({"query": msg})

    return str(response["result"])


# -----------------------------
# Run Flask App
# -----------------------------
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)