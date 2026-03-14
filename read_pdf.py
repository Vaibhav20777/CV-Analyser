import fitz

doc = fitz.open("Vaibhav_CV_Rewritten.pdf")
text = ""

for page in doc :
    text += page.get_text()

print(text)
