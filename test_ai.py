from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)
response = client.chat.completions.create(
        model = "google/gemma-3-4b-it:free",
        messages=[ 
     {"role" : "user" , "content":"Say Hello and tell me a fun fact about Python programming"}
     ]
)
print(response.choices[0].message.content)