# scripts/debug_evaluate_signature.py

from ragas import evaluate
import inspect

print(inspect.signature(evaluate))