from collections import defaultdict

metrics = defaultdict(list)

with open(
    "metrics.log",
    "r",
    encoding="utf-8"
) as file:

    for line in file:

        parts = line.strip().split(",")

        name = parts[-2]
        value = parts[-1]

        metrics[name].append(
            float(value)
        )

print("\n===== DASHBOARD =====\n")

for metric, values in metrics.items():

    avg = sum(values) / len(values)

    minimum = min(values)

    maximum = max(values)

    count = len(values)

    print(
        f"{metric}\n"
        f"  count={count}\n"
        f"  avg={avg:.3f}\n"
        f"  min={minimum:.3f}\n"
        f"  max={maximum:.3f}\n"
    )