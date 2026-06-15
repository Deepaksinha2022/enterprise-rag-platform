# scripts/debug_metric_object.py

from openai import OpenAI

from ragas.llms import llm_factory
from ragas.metrics.collections.faithfulness import Faithfulness

client = OpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1"
)

ragas_llm = llm_factory(
    model="llama3.2",
    provider="openai",
    client=client
)

metric = Faithfulness(
    llm=ragas_llm
)

print(type(metric))
print(metric)