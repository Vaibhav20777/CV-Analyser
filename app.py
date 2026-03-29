from flask import Flask,render_template,request,jsonify
from dotenv import load_dotenv
import os
load_dotenv()
import fitz
from openai import OpenAI
import json
app =  Flask(__name__)
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/analyse",methods=["POST"])
def analyse():
    file = request.files["cv"]
    pdf = fitz.open(stream=file.read(),filetype="pdf")
    text =""
    for page in pdf:
        text += page.get_text()
    job_description = request.form.get("job_description","")
    job_section = f"Job Description:\n{job_description}" if job_description else ""
    prompt = f"""
    Analyse this CV and return ONLY a JSON object with no explanation:
    {{
        "score": 85,
        "summary": "summary here",
        "strengths": ["strength 1", "strength 2"],
        "improvements": ["improvement 1", "improvement 2"],
        "job_match" : null
    }}
    {job_section}

    CV:
    {text}
    """
    response = client.chat.completions.create(
       model = "meta-llama/llama-2-7b-chat:free",
        messages=[{"role": "user","content":prompt}]
    )
    raw = response.choices[0].message.content
    raw = raw.strip().replace("```json", "").replace("```", "").strip()
    result = json.loads(raw)

    return jsonify(result)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)