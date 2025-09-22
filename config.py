import os
from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENROUTER_API_KEY") or "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"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENAI_API_KEY,
)
