import os
import openai

openai.api_key = "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"

print("This is an auto-generated text sequence by openai using their LLM API: ")
response = openai.Completion.create(
    model="text-davinci-003",
    prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.",
    tempurature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human", " AI:"]
)
