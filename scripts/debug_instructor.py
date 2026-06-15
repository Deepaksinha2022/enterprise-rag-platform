# scripts/debug_instructor.py

from ragas.llms import InstructorLLM

import inspect

print(InstructorLLM)
print()
print(inspect.signature(InstructorLLM))