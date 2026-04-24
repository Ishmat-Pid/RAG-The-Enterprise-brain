import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
# REMOVED: from langchain.chains import RetrievalQA  ← You're not using this!

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

        # Modern RAG Prompt
        prompt = ChatPromptTemplate.from_template("""
        Answer the following question based only on the provided context:
        <context>
        {context}
        </context>
        Question: {input}""")

        # Create the modern chain logic
        document_chain = create_stuff_documents_chain(self.llm, prompt)
        retriever = self.vector_db.as_retriever()
        retrieval_chain = create_retrieval_chain(retriever, document_chain)

        response = retrieval_chain.invoke({"input": question})
        return response["answer"]
