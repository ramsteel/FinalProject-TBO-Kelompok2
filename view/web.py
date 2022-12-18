import streamlit as st
import controller.cyk_algorithm.execution as execution
import controller.cyk_algorithm.grammar as grammar
import pandas as pd

# from controller.open_file import open_file
# from controller.raw_conversion import raw_to_cfg
# from controller.cyk_algorithm.cyk_parse import parse

def run_streamlit():
    st.set_page_config(layout='wide')
    
    dct = grammar.getGrammar()
    st.write("<h1 style='text-align:center; '>Pengecekan Kalimat dengan CYK Algorithm</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap='small')

    with col1:
        st.write("### CNF Rules:")
        st.write(dct)

    with col2:
        inputString = st.text_input(' ',placeholder='Masukkan Kalimat Dasar')
        button_click = st.button('Check', type='primary')
        if button_click:
            if len(inputString) == 0: st.write('Kalimat Tidak Boleh Kosong')
            else:
                fillTable = [['' for _ in range(len(inputString.split(' ')))] for _ in range(len(inputString.split(' ')))]
                strTable, flag = execution.exec(dct, fillTable, inputString.lower())
                if flag == True:
                    st.write('<br><h1><font size="5">Filling Table:</font></h2>', unsafe_allow_html=True)
                    st.table(pd.DataFrame(strTable, columns=inputString.split(' ')))
                elif flag == -1:
                    st.write('Maaf, terdapat kata yang tidak sesuai pada rules')
