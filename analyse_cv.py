import fitz
from openai import OpenAI
import json

doc = fitz.open("Vaibhav_CV_Rewritten.pdf")
text = ""

for page in doc :
    text += page.get_text()
prompt = f"""
 You are a professional CV analyser. Analyse the following CV and return ONLY a JSON object with no explanation, no markdown, just pure JSON like this:

{{
    "score": 85,
    "summary": "short summary here",
    "strengths": ["strength 1", "strength 2", "strength 3"],
    "improvements": ["improvement 1", "improvement 2", "improvement 3"]
}}


 CV: 
 {text}
 """

client = OpenAI(
    base_url= "https://openrouter.ai/api/v1",
    api_key= "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"
)
response = client.chat.completions.create(
     model = "google/gemma-3-4b-it:free",
     messages = [{"role": "user","content" : prompt}]

)
raw = response.choices[0].message.content
raw = raw.strip()
raw = raw.replace("```json","").replace("```","")
raw = raw.strip()
result = json.loads(raw)
print("Score:",result["score"])
print("Summary:",result["summary"])
print("Strengths:",result["strengths"])
for s in result["strengths"]:
    print("-",s)
print("Improvements:")
for i in result["improvements"]:
    print(" -",i)
