

import streamlit as st
import controller.cyk_algorithm.execution as execution
import controller.cyk_algorithm.grammar as grammar
from view.displayTable import printFillingTable

def run():
    st.set_page_config(layout='wide')
    
    dct = grammar.getGrammar()  # meminta grammar dari file grammar
    st.write("<h1 style='text-align:center; '>Pengecekan Kalimat dengan CYK Algorithm</h1>", unsafe_allow_html=True)

    st.write('----')

    col1, col2 = st.columns(2, gap='medium') # membagi 1 halaman web menjadi 2 kolom

    with col1:
        st.write('### CNF Rules:')
        details = st.expander('See Details')
        details.write(dct)   # menulis keseluruhan rules

    with col2:
        st.write('###')
        # membuah sebuah input field dengan hint 'Masukkan Kalimat Dasar'
        inputString = st.text_input(' ',placeholder='Masukkan Kalimat Dasar')
        btnClick = st.button('Check', type='primary') # membuah sebuah button dengan text dalam button = 'Check'
        if btnClick:
            if len(inputString) == 0: st.error('_Kalimat Tidak Boleh Kosong_')    # ketika input kosong
            else:
                inputString = inputString.lower()
                x = inputString.split(' ')

                x = [_ for _ in x if _ != '']   # menghilangkan spasi berlebih

                # mendeklarasi sebuah filling table denggan panjang tabel sesuai jumlah kata
                fillTable = [['' for _ in range(len(x))] for _ in range(len(x))]
                stTable, flag = execution.exec(dct, fillTable, x)
                if flag == True:    # ketika string valid akan mencetak tabel
                    st.write('-----')
                    st.write('<h1><font size="5">Filling Table:</font></h2>', unsafe_allow_html=True)
                    st.write(printFillingTable(stTable, x), unsafe_allow_html=True)
                elif flag == -1:    # ketika terdapat kata yang tidak sesuai pada rules
                    st.error('_Maaf, kata "' + stTable + '" tidak ada pada grammar_')
