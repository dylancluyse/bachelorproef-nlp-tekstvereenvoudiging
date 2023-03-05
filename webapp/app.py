from flask import Flask, render_template,request
from langdetect import detect
import nltk, PyPDF2, textstat
import openai, configparser, os

app = Flask(__name__)


"""
used models
"""
COMPLETIONS_MODEL = "text-davinci-003"
EMBEDDING_MODEL = "text-embedding-ada-002"
config = configparser.ConfigParser()

config.read('config.ini')
openai.api_key = config['openai']['api_key']


"""

"""
def pdf_reader():
    pdf_file = request.files['pdf']
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    meta = pdf_reader.metadata
    
    T = ''
    for i in range(pdf_reader.getNumPages()):
            T += pdf_reader.getPage(i).extractText()
    
    lang = detect(T)
    
    return [T, lang, meta]

"""
sends prompt to api
"""
def prompt_gpt(prompt, model, max_tokens, temperature):
    #https://platform.openai.com/docs/api-reference/completions
    return openai.Completion.create(
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            model=model,
            stream=False
        )["choices"][0]["text"].strip(" \n")


"""
index-page
"""
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # pdf_file = request.files['pdf']
        # pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        # meta = pdf_reader.metadata
        # T = ''

        # if True:
        #    for i in range(pdf_reader.getNumPages()):
        #        T += pdf_reader.getPage(i).extractText()
        
        T, lang, meta = pdf_reader()


        T = T.replace('\n', ' ')
        # lang = detect(T)

        # S :> sentences
        S = nltk.sent_tokenize(T)

        # Q :> document
        Q = []
        for s in S:
            s = s.replace("-\n", '')
            # s = s.replace(" ", '')
            fre = textstat.flesch_reading_ease(s)
            Q.append([s, fre])

        params = []
        return render_template('pdf-viewer.html', data=Q, lang=lang, title=meta.title, subject=meta.subject, params=params)
    return render_template('pdf-uploader.html')



"""

"""
@app.route('/quick', methods=['GET','POST'])
def quickSummary():
    T, lang, meta = pdf_reader()
    prompt = "Geef een korte uitleg over het spel 'Phantom Dust' in het Nederlands en maximaal tien woorden lang."
    prompt = f"Vat deze tekst samen met de volgende eisen: "
    result = prompt_gpt(prompt=prompt, max_tokens=20, temperature=0, model=COMPLETIONS_MODEL)
    return render_template('quick-summary.html', result=result, prompt=prompt)

if __name__ == "__main__":
    app.run()