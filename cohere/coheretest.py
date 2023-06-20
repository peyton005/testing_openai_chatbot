import cohere

co = cohere.Client('Vc1UldaD5pMiwOhMg8K3gSNXPajdf1R6GRlc1ejA')

response = co.generate(
    model='xlarge',
    prompt='The rest of this message will be generated using the cohere LLM: ',
    max_tokens=100,
    temperature=1
)

print(response.generations[0].text)