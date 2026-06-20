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

from ragas.run_config import RunConfig

from ragas.metrics import (
    answer_relevancy,
    faithfulness
)

from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)

import logging

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

print("KEY FOUND:", os.getenv("GEMINI_API_KEY") is not None)

# from langchain_openai import ChatOpenAI

df = pd.read_csv(
    "evaluation_results.csv"
).head(1)


print(
    len(
        df["retrieved_context"].str[:1000]
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

from langchain_ollama import ChatOllama

from langchain_community.embeddings import HuggingFaceEmbeddings

# Keep Gemini code commented for fallback
# client = OpenAI(
#     api_key=os.getenv("GEMINI_API_KEY"),
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )
#
# ragas_llm = llm_factory(
#     model="gemini-2.5-flash",
#     provider="openai",
#     client=client
# )

ragas_llm = ChatOllama(
    model="llama3",
    temperature=0
)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Starting evaluation...")

print(dataset[0])

print("ragas type",type(ragas_llm))

print("testing ragas",ragas_llm.invoke("What is 2+2?"))

result = evaluate(
    dataset,
    metrics=[
        answer_relevancy,
        faithfulness
    ],
    llm=ragas_llm,
    embeddings=embeddings,
    run_config=RunConfig(
    max_workers=1,
    timeout=300
)

)

print(result)