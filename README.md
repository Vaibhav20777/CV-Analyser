# CV Analyser

A web application that analyses CVs using AI.

## Features
- Upload a PDF CV
- Get an overall score out of 100
- View strengths and improvements
- Paste a job description to get a match score

## Technologies
- Python, Flask
- PyMuPDF (PDF parsing)
- OpenRouter API (AI analysis)
- HTML, CSS, JavaScript

## How to run
1. Clone the reposit
2. Install dependencies: `pip install -r requirements.txt`
3. Add your OpenRouter API key to a `.env` file
4. Run: `python app.py`
5. Open: `http://localhost:5000`
```

Then run:
```
pip freeze > requirements.txt