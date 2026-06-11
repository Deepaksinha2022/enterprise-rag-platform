from backend.app.services.hybrid_service import (
    hybrid_retrieve
)

from backend.app.services.context_compressor import (
    compress_context
)

results = hybrid_retrieve(
    "annual leave policy"
)

original_size = sum(

    len(chunk)

    for chunk in results
)

compressed = compress_context(
    results
)

compressed_size = sum(

    len(chunk)

    for chunk in compressed
)

reduction = (

    original_size
    -
    compressed_size
)

reduction_percent = (

    reduction
    /
    original_size
) * 100

print("\nCOMPRESSION METRICS\n")

print(
    f"Original Size: {original_size}"
)

print(
    f"Compressed Size: {compressed_size}"
)

print(
    f"Reduction: {reduction}"
)

print(
    f"Reduction %: {reduction_percent:.2f}%"
)