1. Overview

Briefly describe the project.

Enterprise RAG Platform is a production-oriented Retrieval-Augmented Generation system built with FastAPI, ChromaDB, Sentence Transformers, BM25, Hybrid Retrieval, JWT Authentication, RBAC, LangSmith observability, Docker, and CI/CD automation. The platform enables secure document ingestion, retrieval, and question-answering workflows.

2. Features

List major capabilities.

Document ingestion
ChromaDB vector storage
BM25 retrieval
Hybrid retrieval
RAG pipeline
JWT authentication
RBAC authorization
LangSmith observability
RAGAS evaluation
Docker deployment
CI/CD automation
3. Tech Stack

Summarize technologies.

Backend: FastAPI
Vector Database: ChromaDB
Embeddings: Sentence Transformers
Retrieval: BM25 + Hybrid Search
Authentication: JWT + RBAC
Observability: LangSmith
Evaluation: RAGAS
Containerization: Docker, Docker Compose
CI/CD: GitHub Actions

4. Architecture

Describe the flow.

User requests are authenticated through JWT-based security. Queries pass through the hybrid retrieval layer combining vector search and BM25 retrieval. Retrieved context is supplied to the LLM for response generation. LangSmith captures traces while RAGAS is used for evaluation and regression testing.

5. Project Structure

Explain major folders.

backend/
frontend/
data/
tests/
docs/
infrastructure/
scripts/

Briefly explain each folder's purpose.

6. Local Setup

Provide installation instructions.

git clone <repo>
cd enterprise-rag-platform

python -m venv .venv
pip install -r backend/requirements.txt

uvicorn backend.app.main:app --reload

Mention .env configuration.

7. API Endpoints

Document key endpoints.

Endpoint	Method	Purpose
/	GET	Root endpoint
/health	GET	Health check
/docs	GET	Swagger UI
Your RAG endpoints	POST	Question answering
8. Example Workflow

Explain end-to-end usage.

Upload documents
Generate embeddings
Store vectors in ChromaDB
Submit query
Retrieve relevant context
Generate answer
Observe traces in LangSmith
9. Evaluation Results

Summarize RAGAS work.

The platform was evaluated using RAGAS metrics including Faithfulness, Answer Relevance, and Context Precision. Regression testing was implemented to ensure retrieval and generation quality remained stable across updates.

10. Deployment

Describe deployment status.

The application is containerized using Docker and Docker Compose. CI/CD pipelines are implemented with GitHub Actions. The platform has been deployed and validated in a cloud environment using Railway.

11. Future Enhancements

List next-stage improvements.

Redis caching
Multi-tenant support
Streaming responses
Advanced reranking
Kubernetes deployment
Additional evaluation datasets
Cost monitoring dashboards

After this, your README is essentially portfolio-ready.


## Architecture

![Architecture](docs/architecture.png)

## Performance Metrics

| Metric | Value |
|----------|----------|
| Cache Hit Ratio | Tracked |
| Semantic Cache Hits | Tracked |
| LLM Calls Saved | Tracked |
| Retrieval Latency | Tracked |
| LLM Latency | Tracked |
| Request Latency | Tracked |
| Estimated Cost/Query | Tracked |
| SSE Streaming | Implemented |
| TTFT | 3.586s |
| Semantic Cache Similarity Threshold | 0.80 |


## Optimizations Implemented

- Redis Exact Match Cache
- Semantic Cache (Sentence Transformers)
- Async Embedding Generation
- Concurrent Embeddings using run_in_executor
- SSE Streaming
- True Ollama Streaming
- Cost Tracking
- Latency Tracking

## RAG Evaluation

| Metric | Score |
|----------|----------|
| Answer Relevancy | 0.8425 |


## Evaluation Metrics

| Metric | Score |
|---------|---------|
| Answer Relevancy (Gemini) | 0.8006 |
| Answer Relevancy (Local Llama3.2) | 0.6431 |

Evaluation Stack:
- RAGAS
- Ollama Llama3.2
- all-MiniLM-L6-v2 Embeddings
- LangSmith Tracing

## Performance Metrics

## Performance Metrics

| Metric | Value |
|----------|----------|
| Precision@5 | 0.145 |
| Recall@5 | 0.725 |
| HitRate@5 | 0.725 |
| Precision@10 | 0.0848 |
| Recall@10 | 0.8485 |
| HitRate@10 | 0.8485 |
| Avg Request Latency | 14.17 sec |
| P50 Request Latency | 11.29 sec |
| P95 Request Latency | 22.13 sec |
| P99 Request Latency | 52.37 sec |
| Avg Retrieval Latency | 1.72 sec |
| P50 Retrieval Latency | 0.90 sec |
| P95 Retrieval Latency | 5.92 sec |
| P99 Retrieval Latency | 7.90 sec |
| Avg LLM Latency | 12.39 sec |
| P50 LLM Latency | 10.35 sec |
| P95 LLM Latency | 19.77 sec |
| P99 LLM Latency | 45.14 sec |
| Cache Hit Ratio | 71.43% |
| Estimated Cost / Query | $0.000242 |
| Evaluation Dataset Size | 33 Questions |
| Retrieval Method | Hybrid (BM25 + Dense) |
| Embedding Model | all-MiniLM-L6-v2 |
| LLM | Llama 3.2 (Ollama) |