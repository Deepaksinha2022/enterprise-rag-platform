# scripts/debug_llm_factory.py

from ragas.llms import llm_factory

import inspect

print(inspect.signature(llm_factory))