# scripts/debug_metric_check.py

from ragas.metrics.base import Metric
from ragas.metrics.collections.faithfulness import Faithfulness

print(
    issubclass(
        Faithfulness,
        Metric
    )
)