# scripts/debug_faithfulness.py

from ragas.metrics.collections.faithfulness import Faithfulness
import inspect

print(inspect.signature(Faithfulness))