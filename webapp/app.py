# Web-app imports
from flask import Flask, render_template,request

# PDF Miner
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from io import BytesIO

# 
from langdetect import detect
import fitz, nltk, openai, configparser, os, spacy

# import nltk, PyPDF2, textstat
# import openai, configparser, os

app = Flask(__name__)

"""
used gpt-3 models
"""
COMPLETIONS_MODEL = "text-davinci-003"
EMBEDDING_MODEL = "text-embedding-ada-002"
config = configparser.ConfigParser()

config.read('config.ini')
openai.api_key = config['openai']['api_key']


"""

"""
def get_full_text(all_pages):
    total = ""

    for page_layout in all_pages:
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    total += text_line.get_text()

    # total = ' '.join(total)
    return nltk.sent_tokenize(total)



"""

"""
def get_toc(document):
    arr_outlines = []
    if "Outlines" in document.catalog:
        outlines = document.get_outlines()
        for (level,title,dest,a,se) in outlines:
            arr_outlines.append([level, title])


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/view-pdf', methods=['GET','POST'])
def show_pdf():
    pdf = request.files['pdf']
    pdf_data = BytesIO(pdf.read())

    # parser = PDFParser(fp)
    # document = PDFDocument(parser)

    all_pages = extract_pages(
        pdf_data,
        page_numbers=None,
        maxpages=5
    )

    sentences = get_full_text(all_pages)

    return render_template(
        'pdf-viewer.html',
        full_text = sentences
    )


"""
def pdf_reader():
    pdf_file = request.files['pdf']
    pdf = fitz.open(pdf_file)
    meta = pdf.metadata
    return [T, lang, meta]


def data_clean_and_sentences(T):
    T = T.replace('\n', ' ')
    S = nltk.sent_tokenize(T)
    Q = []
    for s in S:
        s = s.replace("-\n", '')
        fre = textstat.flesch_reading_ease(s)
        Q.append([s, fre])
    return Q

def prompt_gpt(prompt, model, max_tokens, temperature):
    #https://platform.openai.com/docs/api-reference/completions
    return openai.Completion.create(
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            model=model,
            stream=False
        )["choices"][0]["text"].strip(" \n")

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':       
        T, lang, meta = pdf_reader()
        Q = data_clean_and_sentences(T)
        params = []
        return render_template('pdf-viewer.html', data=Q, lang=lang, title=meta.title, subject=meta.subject, params=params)
    return render_template('index.html')

@app.route('/quick', methods=['GET','POST'])
def quickSummary():
    T, lang, meta = pdf_reader()

    prompt = f"Vat deze tekst samen in 1 paragraaf van 10 zinnen en zorg ervoor dat iedere zin max 10 woorden lang is: context: {T}"
    result = prompt_gpt(
        prompt=prompt, 
        max_tokens=500, 
        temperature=0, 
        model=COMPLETIONS_MODEL
    )

    prompt = f"
        Vereenvoudig deze tekst met deze parameters:
        Zin is max {amount_words_sentence} woorden lang
        Max {amount_sentences} aantal zinnen.
        Schrijf dit met zo een eenvoudig mogelijke woordenschat.
        context: 
        {T}
    "

    Q = data_clean_and_sentences(T)
    R = data_clean_and_sentences(result)
    R2 = data_clean_and_sentences(result2)

    print(Q)
    print(R)
    print(R2)

    return render_template('quick-summary.html', original=Q, result=R, result2=R2, lang=lang)
"""

if __name__ == "__main__":
    app.run()
