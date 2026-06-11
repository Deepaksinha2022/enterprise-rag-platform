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

Enterprise RAG Platform v2

Features:

- PDF ingestion
- Semantic chunking
- ChromaDB vector storage
- BM25 retrieval
- Hybrid retrieval (BM25 + Vector Search)
- Metadata filtering
- Citation generation
- Retrieval benchmarking
- FastAPI API
- Ollama integration

Metrics:

Top-1 Accuracy: 100%
Recall@3: 100%

Architecture:

User Query
    ↓
Hybrid Retrieval
(BM25 + Vector)
    ↓
Fusion Layer
    ↓
Context Builder
    ↓
Ollama
    ↓
Answer

# Enterprise RAG Platform v2

## Features

* PDF ingestion pipeline
* Document chunking
* Sentence Transformer embeddings
* ChromaDB vector storage
* BM25 retrieval
* Hybrid retrieval (BM25 + Vector Search)
* Metadata filtering
* Citation generation
* Retrieval benchmarking
* Ollama local LLM integration
* FastAPI REST API

## Evaluation

* Top-1 Accuracy: 100%
* Recall@3: 100%

## Tech Stack

* Python
* FastAPI
* ChromaDB
* Sentence Transformers
* BM25
* Ollama
* LangChain

## Future Enhancements

* Hybrid retrieval with metadata-aware citations
* Reranking
* Multi-document corpora
* RBAC access control
* Streamlit UI


# Enterprise RAG Platform v3

## Overview

Enterprise-grade Retrieval-Augmented Generation (RAG) system supporting hybrid retrieval, reranking, query enhancement, prompt management, and hallucination reduction.

## Features

- PDF Ingestion
- Document Chunking
- SentenceTransformer Embeddings
- ChromaDB Vector Store
- BM25 Retrieval
- Hybrid Retrieval
- CrossEncoder Reranking
- Query Rewriting
- Query Expansion
- Metadata Filtering
- Citation Generation
- Hallucination Guardrails
- Prompt Versioning
- Context Compression
- Latency Optimization

## Architecture

[Architecture Diagram]

## Evaluation

Top-1 Accuracy: 100%
Recall@3: 100%
Prompt Compression: ~42%
Latency: 8.3s → 1.3s

## Tech Stack

Python
FastAPI
ChromaDB
SentenceTransformers
BM25
Ollama
LangChain

## Future Work

- Multi-document corpora
- RBAC access control
- Advanced metadata filtering
- Production deployment