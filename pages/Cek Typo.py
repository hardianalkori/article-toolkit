import streamlit as st
import pandas as pd
import re

st.set_page_config(
    page_title = "Article Toolkit | Deteksi Typo")

st.title("Deteksi Typo Sederhana")

gabung = pd.read_excel("kamus.xlsx")
gabung = gabung.values[:,0].astype(str).tolist()

def bersih(data):
	data = re.sub(r"[^a-zA-Z- ]","",data).lower().split()
	return data

def levenshtein_distance(str1, str2):
    m, n = len(str1) + 1, len(str2) + 1 #deklarasi m panjang str1 dan n str1 
    matrix = [[0 for _ in range(n)] for _ in range(m)] # buat matriks ukuran mxn
    
    for i in range(m):
        matrix[i][0] = i #untuk mengisi nilai 1-nm pada baris
    for j in range(n):
        matrix[0][j] = j #untuk mengisi nilai 1-nn pada kolom	
    
    for i in range(1, m): #iterasi baris
        for j in range(1, n): # iterasi kolom
            cost = 0 if str1[i - 1] == str2[j - 1] else 1 # cost 0 jika karakter sama
            matrix[i][j] = min(matrix[i - 1][j] + 1,
                               matrix[i][j - 1] + 1,
                               matrix[i - 1][j - 1] + cost)
    
    return matrix[-1][-1] #mengembalikan nilai  matrix paling akhir paling kanan bawah

def cek_typo(kata_artikel, corpus):
    mirip = min(corpus, key=lambda x: levenshtein_distance(str(kata_artikel), str(x)))
    return mirip



text_input = st.text_area(label='Enter your text here:')

if st.button(label='Cek Sekarang'):
    text = bersih(text_input)
    st.title("Typo yang terdeteksi:")
    for i in text:
        if i not in gabung:
            cek = cek_typo(i, gabung)
            st.write(i,":",cek)
        else:
            continue