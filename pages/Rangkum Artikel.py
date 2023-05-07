import streamlit as st
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory,ArrayDictionary,StopWordRemover
import pandas as pd
import numpy as np

st.set_page_config(
    page_title = "Article Toolkit | Rangkum Artikel")

st.title("Rangkum Artikel")

sw = pd.read_excel("stopwords.xlsx",header = None).values[:,0].tolist()

stop = StopWordRemoverFactory().get_stop_words()
data = stop + sw
data = ArrayDictionary(data)
word = StopWordRemover(data)



def preprocess_artikel(data):
    data = re.sub(r"[^A-Za-z., ]","",data)
    #data = re.sub(r"\b\w{1}\b","",data)
    data = re.sub(' +', ' ',data)
    return data

def rangkum(teks):
    teks = teks.split(".")
    tfidf = TfidfVectorizer()
    tf = tfidf.fit_transform(teks).toarray()
    n = len(teks)//2
    hasil = np.sum(tf,axis = 1)
    penting = np.argsort(hasil)[-n:]
    index_penting = sorted(penting)

    rangkum = [teks[i] for i in index_penting]
    print(rangkum)
    return ". ".join(rangkum)

mentah = st.text_area(label='Enter your text here:')

if st.button(label='Rangkum Artikel'):
    artikel_mentah = preprocess_artikel(mentah)
    hasil_rangkum = rangkum(artikel_mentah)
    st.write(hasil_rangkum)
