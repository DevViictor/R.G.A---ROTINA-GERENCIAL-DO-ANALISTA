import streamlit as st
import pandas as pd
from streamlit_extras.colored_header import colored_header
from st_aggrid import AgGrid,GridOptionsBuilder


def contagem():

    st.set_page_config(page_title="Auxilar de Estoque", layout="wide")

    colored_header(
        label="R.G.A - Auxíliar de estoque",
        description="Auxíliar de estoque",
        color_name="orange-70"
    )
        
    df = st.file_uploader("Carregue o arquivo abaixo: ",type=["xlsx", "xls"])

    if df is not None:
        leitor_sap  = pd.read_excel(df)

        st.text_input("Digite o codigo do produto")

        AgGrid(leitor_sap)
    
    else:
        st.warning("Selecione a planilha que deseja visualizar")

    

    