import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
<<<<<<< HEAD
=======

# UPDATED IMPORT FOR 2026
from langchain.chains.retrieval_qa.base import RetrievalQA 
>>>>>>> origin/main

load_dotenv()

class EnterpriseBrain:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0)
        self.vector_db = None

    def process_pdf(self, file_path):
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_documents(docs)
        
        self.vector_db = Chroma.from_documents(
            documents=chunks, 
            embedding=self.embeddings, 
            persist_directory="./db"
        )
        return "Success: Enterprise Brain is now trained."

    def ask_question(self, question):
        if not self.vector_db:
            return "Please upload a document first."
        
        docs = self.vector_db.similarity_search(question, k=3)
        context = "\n\n".join([doc.page_content for doc in docs])
        
        prompt = f"""Answer based only on this context:

{context}

Question: {question}

Answer:"""
        
        response = self.llm.invoke(prompt)
        return response.content
