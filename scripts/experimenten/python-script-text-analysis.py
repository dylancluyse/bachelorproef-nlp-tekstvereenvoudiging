from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar
import spacy
from langdetect import detect
import pandas as pd
import os
import readability


folder_path = 'scripts\experimenten\pdf'
dutch_spacy_model = "nl_core_news_md"
english_spacy_model = "en_core_web_md"

dict = {
    'nl':'nl_core_news_md',
    'en':'en_core_web_md'
}

total_df = None

"""
"""
def get_sentence_length(sentence):
    doc = nlp(sentence)
    return len(doc)

"""
"""
pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

"""
"""
for pdf in pdf_files:

    print(pdf)

    """
    """
    all_pages = extract_pages(
        pdf_file='scripts\experimenten\pdf/'+ pdf,
        page_numbers=[0],
        maxpages=999
    )

    full_text = ""
    for page_layout in all_pages:
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    full_text += text_line.get_text()

    """
    """
    full_text = full_text.strip()
    full_text = full_text.replace('\n', ' ')
    lang = detect(full_text)

    """
    """
    model = dict.get(detect(full_text))
    nlp = spacy.load(model)
    doc = nlp(full_text)

    sentences = []
    for sentence in doc.sents:
        sentences.append(str(sentence))

    """
    Dataframe opbouwen voor een pdf. Hieronder wordt de zin, bron en zinlengte opgeslaan.
    """
    df = pd.DataFrame(sentences, columns=['sentence'])
    df['source'] = pdf.split('_')[0]
    df['title'] = pdf.split('_')[1]
    df['sentence_length'] = df['sentence'].apply(get_sentence_length)


    """
    Filteren. Zinnen kleiner dan 3 woord-tokens zijn niet mogelijk. Deze worden verworpen.
    """
    df = df[df['sentence_length'] > 3]   


    """
    """
    for key in readability.getmeasures("test")['readability grades'].keys():
        df[key] = df['sentence'].apply(lambda x: readability.getmeasures(x)['readability grades'][key])

    """
    """
    word_usage_cols = readability.getmeasures("test")['word usage'].keys()
    for key in word_usage_cols:
        df[key] = df['sentence'].apply(lambda x: readability.getmeasures(x, lang=lang)['word usage'][key])

    """
    """
    sentence_beginnings_cols = readability.getmeasures("test")['sentence beginnings'].keys()
    for key in sentence_beginnings_cols:
        df[key] = df['sentence'].apply(lambda x: readability.getmeasures(x, lang=lang)['sentence beginnings'][key])

    """
    """
    if total_df is None:
        total_df = df
    else:
        if not df.empty:
            total_df = pd.concat([total_df, df], ignore_index=True)


total_df.to_csv(path_or_buf='text-analysis-simplification.csv', index=False)