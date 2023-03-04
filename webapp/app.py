from flask import Flask, render_template,request
import PyPDF2
import nltk

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pdf_file = request.files['pdf']
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        text = ''

        for i in range(pdf_reader.getNumPages()):
            text += pdf_reader.getPage(i).extractText()
        
        # zorgen dat de zinnen aan elkaar plakken
        text = text.replace('\n', ' ')

        # teruggeven als een array van zinnen
        nltk.download('punkt')
        sentences = nltk.sent_tokenize(text)

        #print(sentences)

        return render_template('pdf_viewer.html', text=sentences)
    return render_template('pdf_uploader.html')


if __name__ == "__main__":
    app.run()