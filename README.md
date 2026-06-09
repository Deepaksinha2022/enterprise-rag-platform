# Enterprise RAG Platform

## Overview

Enterprise RAG Platform is a Retrieval-Augmented Generation (RAG) application built using FastAPI, ChromaDB, Sentence Transformers, and Ollama.

The system allows users to upload PDF documents, ingest them into a vector database, retrieve relevant information using semantic search, and generate grounded responses using a local LLM.

---

## Features

* PDF Upload API
* Document Ingestion Pipeline
* Recursive Text Chunking
* Metadata Enrichment
* Embedding Generation (MiniLM)
* Chroma Vector Database
* Semantic Retrieval (Top-K Search)
* Prompt Templates
* Local LLM Integration (Ollama + Llama 3.2)
* FastAPI REST Endpoints

---

## Architecture

PDF Upload

→ Document Loader

→ Chunking

→ Metadata

→ Embeddings

→ ChromaDB

→ Retriever

→ Prompt Builder

→ Llama 3.2

→ Answer

---

## Tech Stack

* Python
* FastAPI
* ChromaDB
* Sentence Transformers
* Ollama
* Llama 3.2
* Uvicorn

---

## Run Locally

Install dependencies:

pip install -r requirements.txt

Start API:

uvicorn backend.app.main:app --reload

Open:

http://127.0.0.1:8000/docs

---

## Example Flow

1. Upload PDF
2. Run ingestion pipeline
3. Ask question
4. Retrieve relevant chunks
5. Generate grounded answer

---

## Future Improvements

* Hybrid Search
* Re-ranking
* Multi-document Retrieval
* Conversation Memory
* Production Deployment
* Monitoring & Observability


Project Overview
Architecture Diagram
Tech Stack
Setup Instructions
Example Query
Future Improvements