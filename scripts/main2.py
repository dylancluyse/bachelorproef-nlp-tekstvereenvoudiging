import spacy
from fastapi import FastAPI, Form
from fastapi import HTTPException
from fastapi import Depends, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load the Dutch spaCy model for text simplification
nlp = spacy.load("nl_core_news_md")

def simplify_text(text: str) -> str:
    # Tokenize and lemmatize the text
    doc = nlp(text)
    lemmas = [token.lemma_.lower() for token in doc]
    # Remove stop words and punctuation
    words = [lemma for lemma in lemmas if lemma not in nlp.Defaults.stop_words and lemma.isalpha()]
    # Rejoin the words into a single string
    simplified_text = " ".join(words)
    return simplified_text

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("simplify.html", {"request": request})

@app.post("/simplify")
async def simplify(text: str = Form(...)):
    simplified_text = simplify_text(text)
    return {"simplified_text": simplified_text}
