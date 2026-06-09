# Enterprise RAG Platform Architecture

```text
                    +------------------+
                    |   User Uploads   |
                    |      PDF         |
                    +--------+---------+
                             |
                             v
                    +------------------+
                    | Document Loader  |
                    |  PyPDFLoader     |
                    +--------+---------+
                             |
                             v
                    +------------------+
                    | Recursive        |
                    | Chunking         |
                    +--------+---------+
                             |
                             v
                    +------------------+
                    | Metadata         |
                    | Enrichment       |
                    +--------+---------+
                             |
                             v
                    +------------------+
                    | Embedding Model  |
                    | MiniLM           |
                    +--------+---------+
                             |
                             v
                    +------------------+
                    | ChromaDB         |
                    | Vector Store     |
                    +--------+---------+
                             ^
                             |
                    Query Embedding
                             |
                             |
+-------------+    +--------+---------+
| User Query  |--->| Retriever        |
+-------------+    | Top-K Search     |
                   +--------+---------+
                            |
                            v
                   +------------------+
                   | Context Builder  |
                   +--------+---------+
                            |
                            v
                   +------------------+
                   | Prompt Template  |
                   +--------+---------+
                            |
                            v
                   +------------------+
                   | Llama 3.2        |
                   | (Ollama)         |
                   +--------+---------+
                            |
                            v
                   +------------------+
                   | Final Answer     |
                   +------------------+
```