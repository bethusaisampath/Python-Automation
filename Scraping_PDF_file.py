import fitz

with fitz.open("students.pdf") as pdf:
  text = ''
  for page in pdf:
    text = text + page.get_text()
    print(text)
    