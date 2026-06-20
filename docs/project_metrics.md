# Enterprise RAG Platform Metrics Log

## Task 3 - Caching

- Semantic Cache Implemented
- Similarity Threshold: 0.80
- Semantic Cache Hits: Working
- LLM Calls Saved: Working

## Task 4 - Streaming

- SSE Streaming: Implemented
- True Ollama Streaming: Implemented
- TTFT Before: 38.779s
- TTFT After: 3.586s
- Improvement: ~90%

## Task 5 - Latency Benchmarking

### Request Latency

- Average: 14.167s
- Min: 4.881s
- Max: 59.928s
- P50: 11.294s
- P95: 22.131s
- P99: 52.369s

### Retrieval Latency

- Average: 1.722s
- Min: 0.614s
- Max: 8.400s
- P50: 0.901s
- P95: 5.922s
- P99: 7.904s

### LLM Latency

- Average: 12.389s
- Min: 4.124s
- Max: 51.485s
- P50: 10.346s
- P95: 19.770s
- P99: 45.142s

## Performance Benchmarks

| Metric | Value |
|----------|----------|
| Request Latency P50 | 11.294s |
| Request Latency P95 | 22.131s |
| Request Latency P99 | 52.369s |
| Retrieval Latency P50 | 0.901s |
| Retrieval Latency P95 | 5.922s |
| Retrieval Latency P99 | 7.904s |
| LLM Latency P50 | 10.346s |
| LLM Latency P95 | 19.770s |
| LLM Latency P99 | 45.142s |
| TTFT | 3.586s |
| Semantic Cache | Implemented |
| SSE Streaming | Implemented |

## Task 6 - RAGAS Evaluation

### Answer Relevancy

Score: 0.8425

Evaluation Model:
- Gemini 2.5 Flash

Embedding Model:
- sentence-transformers/all-MiniLM-L6-v2

Dataset Size:
- 2 evaluation samples (test run)

Status:
- Passed

## Task 6 - RAGAS Evaluation

### Answer Relevancy

| Run | Model | Score |
|------|--------|--------|
| 1 | Gemini 2.5 Flash | 0.8006 |
| 2 | Ollama Llama3.2 | 0.4701 |
| 3 | Ollama Llama3.2 | 0.6431 |

Status: Completed