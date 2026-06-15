from openai import OpenAI

from langchain_openai import OpenAIEmbeddings

import pandas as pd

from datasets import Dataset

from ragas import evaluate

from ragas.llms import llm_factory

# from ragas.llms import LangchainLLMWrapper

from ragas.metrics import answer_relevancy

import os

from dotenv import load_dotenv

load_dotenv()

print("KEY FOUND:", os.getenv("GEMINI_API_KEY") is not None)

# from langchain_openai import ChatOpenAI

df = pd.read_csv(
    "evaluation_results.csv"
).head(1)

print(
    len(
        df["retrieved_context"].iloc[0]
    )
)

dataset = Dataset.from_dict(
    {
        "question": df["question"].tolist(),
        "answer": df["generated_answer"].tolist(),
        "contexts": [
            [c]
            for c in df["retrieved_context"]
        ],
        "ground_truth": df[
            "ground_truth"
        ].tolist()
    }
)

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

ragas_llm = llm_factory(
    model="gemini-2.5-flash",
    provider="openai",
    client=client
)
print(type(answer_relevancy.embeddings))

embeddings = OpenAIEmbeddings(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    model="text-embedding-3-small"
)

result = evaluate(
    dataset,
    metrics=[
        answer_relevancy
    ],
    llm=ragas_llm,
    embeddings=embeddings
)

print(result)

