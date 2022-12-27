import re
from fastapi import FastAPI, Form

app = FastAPI()

import spacy
from spacy.lang.nl import Dutch
from spacy.matcher import Matcher

nlp = spacy.load('nl_core_news_md')

def simplify_text(text):
  doc = nlp(text)
  
  # Replace long and complex sentences with shorter ones
  for sent in doc.sents:
    if len(sent) > 15:
      sent.merge(sent[:15], sent[15:])
  
  # Replace difficult vocabulary with simpler words or phrases
  matcher = Matcher(nlp.vocab)
  patterns = [
      [{"LOWER": "gebruik"}, {"LOWER": "dit"}, {"LOWER": "hulpmiddel"}],
      [{"LOWER": "voldoende"}, {"LOWER": "middelen"}]
  ]
  matcher.add("MoeilijkVocaabulaire", None, *patterns)
  for match_id, start, end in matcher(doc):
    span = doc[start:end]
    span.merge(span[:2], span[2:])
  
  # Reorganize the structure of the text to make it easier to follow
  doc = list(doc)
  new_doc = []
  for word in doc:
    if word.text == "\n":
      new_doc.append(word.text.replace("\n", " "))
    else:
      new_doc.append(word.text)
  doc = " ".join(new_doc)
  
  return doc

@app.get("/simplify")
async def simplify(text: str = Form(...)):
    simplified_text = simplify_text(text)
    return {'text': text, 'simplified_text': simplified_text}

@app.post("/form")
def display_form_content(name: str = Form(...)):
    return {"name": name}

@app.get("/")
async def index():
    return {'name': "test"}