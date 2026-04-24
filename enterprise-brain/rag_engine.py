
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains.retrieval_qa.base import RetrievalQA

load_dotenv()

class EnterpriseBrain:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)
        self.vector_db = None

    def process_pdf(self, file_path):
        # 1. Load PDF
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        
        # 2. Chunking (Pro-tip: 1000 char chunks with overlap)
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_documents(docs)
        
        # 3. Create Vector Store (Saves locally in 'db' folder)
        self.vector_db = Chroma.from_documents(
            documents=chunks, 
            embedding=self.embeddings, 
            persist_directory="./db"
        )
        return "Success: Brain indexed."

    def ask_question(self, question):
        if not self.vector_db:
            return "Please upload a document first."
        
        # 4. Retrieval QA Chain (with Source Citations)
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_db.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=True
        )
        
        result = qa_chain.invoke({"query": question})
        answer = result["result"]
        source = result["source_documents"][0].metadata.get("page", "Unknown")
        
        return f"{answer} (Source: Page {source+1})"