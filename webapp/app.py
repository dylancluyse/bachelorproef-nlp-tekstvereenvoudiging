# Web-app imports
from flask import Flask, render_template,request,jsonify

# PDF Miner
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from io import BytesIO

# 
from langdetect import detect
import fitz, nltk, openai, configparser, os, spacy, re, yake
from summarizer import Summarizer

# import nltk, PyPDF2, textstat
# import openai, configparser, os

app = Flask(__name__)

"""
used gpt-3 models
"""
# COMPLETIONS_MODEL = "gpt-3.5-turbo"
COMPLETIONS_MODEL = "text-davinci-003"
EMBEDDING_MODEL = "text-embedding-ada-002"
config = configparser.ConfigParser()
config.read('config.ini')
openai.api_key = config['openai']['api_key']


"""
Return ten keywords
"""
def get_keywords(text_without_stopwords):
    language = "nl"
    max_ngram_size = 1
    deduplication_threshold = 0.9
    numOfKeywords = 10
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(text_without_stopwords)
    return keywords


"""

"""
def get_full_text(all_pages):
    total = ""
    for page_layout in all_pages:
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    total += text_line.get_text()
                    total = re.sub('(.{0})-\s*', '', total) # sommige lijnen worden afgebroken door een liggend streepje --> preventie
    nlp = spacy.load("nl_core_news_sm") if detect(total) == 'nl' else spacy.load("en_core_word_md")
    
    doc = nlp(total)
    word_arrays = []

    for sent in doc.sents:
        word_array = [token.text for token in sent]
        word_arrays.append(word_array)

    return word_arrays


"""
"""
def prompt_gpt(prompt, model, max_tokens, temperature):
    # https://platform.openai.com/docs/api-reference/completions
    return openai.Completion.create(
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            model=model,
            top_p=0.9,
            stream=False
        )["choices"][0]["text"].strip(" \n")

"""

"""
def get_summary_of_abstract(all_pages):
    total = ""
    for page_layout in all_pages:
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    total += text_line.get_text()
                    total = re.sub('(.{0})-\s*', '', total)
    total = "".join(total)
    print(total[:400])
    prompt = f"""
    Schrijf dit zo eenvoudig mogelijk. Gebruik eenvoudige woordenschat en zinnen die niet langer dan 10 woorden zijn. Vermeld zeker de probleemstelling, resultaten en conclusie.
    context:
    {total[:400]}
    """
    return [total, prompt_gpt(prompt=prompt, model=COMPLETIONS_MODEL, max_tokens=999, temperature=0)]


"""
todo
"""
def get_toc(document):
    arr_outlines = []
    if "Outlines" in document.catalog:
        outlines = document.get_outlines()
        for (level,title,dest,a,se) in outlines:
            arr_outlines.append([level, title])

"""

"""
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

"""
"""
@app.route('/view-pdf', methods=['GET','POST'])
def show_pdf():
    pdf = request.files['pdf']
    pdf_data = BytesIO(pdf.read())

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
"""
@app.route('/quick', methods=['GET','POST'])
def summarize_abstract():
    pdf = request.files['pdf']
    pdf_data = BytesIO(pdf.read()) 
    all_pages = extract_pages(
        pdf_data,
        page_numbers=None,
        maxpages=5
    )
    original, result = get_summary_of_abstract(all_pages=all_pages)
    return render_template('quick-summary.html', result=result, original=original)


@app.route('/look-up-word',methods=['GET'])
def look_up_word():
    word = request.args.get('word')
    context = request.args.get('context')
    prompt = f"""Leg {word} uit in de context van "{context}"? Geef een uitleg  max. 1 zin en 1 voorbeeld. Geef 3 eenvoudigere synoniemen"""
    result = prompt_gpt(
            prompt=prompt,
            max_tokens=200,
            model=COMPLETIONS_MODEL,
            temperature=0)
    return jsonify(result=result, prompt=prompt)


@app.route('/summarize',methods=['GET'])
def summarize():
    text = request.args.get('text')
    sentences = 5
    max_words = 10
    prompt = f"""
    Vat deze tekst samen in max {sentences} zinnen en max {max_words} woorden per zin.
    context:
    {text}
    """
    text = prompt_gpt(
        model=COMPLETIONS_MODEL,
        max_tokens=500,
        prompt=prompt,
        temperature=0
    )

    return jsonify(result=text, prompt=prompt)

@app.route('/extract-text', methods=['GET'])
def extract():
    text = request.args.get('text')
    # sents = nltk.sent_tokenize(text)
    
    summarizer = Summarizer()
    result = summarizer(
        #algorithm=...,
        body=text,
        #max_length=460,
        min_length=100,
        num_sentences=10,
        #ratio=...,
        #return_as_list=...,
        #use_first=...,
    )
    return jsonify(result=result)


@app.route('/syntactic-simplify', methods=['GET'])
def syntactic_simplify():
    text = request.args.get('text')
    max_words = 10
    prompt = f"""
    Breek zinnen langer dan {max_words} woorden op. Verander verwijswoorden naar de oorspronkelijke naam.
    Vervang tangconstructies door de bijzin naar het begin of het einde te plaatsen. 
    Vervang voorzetseluitdrukkingen en samengestelde werkwoorden.
    context:
    {text}
    """
    text = prompt_gpt(
        model=COMPLETIONS_MODEL,
        max_tokens=500,
        prompt=prompt,
        temperature=0
    )
    return jsonify(result=text, prompt=prompt)

@app.route('/foo', methods=['GET'])
def foo():
    return render_template('tryout.html')

if __name__ == "__main__":
    app.run()

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

