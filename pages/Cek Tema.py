import streamlit as st
import re
import joblib
import pandas as pd
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory,ArrayDictionary,StopWordRemover

st.set_page_config(
    page_title = "Article Toolkit | Deteksi Tema")

st.title("Deteksi Tema Artikel")

sw = pd.read_excel("sw.xlsx",header = None).values[:,0].tolist()

model = joblib.load("rfc.joblib")
idf = joblib.load("idf.joblib")

stop = StopWordRemoverFactory().get_stop_words()
data = stop + sw
data = ArrayDictionary(data)
word = StopWordRemover(data)


def sword(data):
    data = word.remove(data)
    data = data.strip()
    return data

def preprocess_artikel(data):
	data = data.lower()
	data = re.sub(r"[^a-z ]", " ", data)
	data = re.sub(r"\b\w{1}\b","",data)
	data = re.sub(' +', ' ',data)
	return data

text = st.text_area(label='Enter your text here:')

if st.button(label='Cek Tema'):
	artikel = preprocess_artikel(text)
	artikel = sword(artikel)
	artikel_idf = idf.transform([artikel])
	deteksi = model.predict(artikel_idf)
	st.title("Tema Yang Terdeteksi:")
	st.write(deteksi[0])