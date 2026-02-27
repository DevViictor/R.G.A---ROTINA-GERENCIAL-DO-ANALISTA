import streamlit as st
import pandas as pd
from streamlit_extras.colored_header import colored_header
from streamlit_extras.metric_cards  import style_metric_cards
from st_aggrid import AgGrid,GridOptionsBuilder
from datetime import datetime


def contagem():

    st.set_page_config(page_title="Auxilar de Estoque", layout="wide")

    colored_header(
        label="Auxíliar de estoque",
        description="Auxíliar de estoque",
        color_name="orange-70"
    )
        
    df = st.file_uploader("Carregue o arquivo abaixo: ",type=["xlsx", "xls"])

    if df is not None:

        filtro = st.text_input("Digite o material do produto que deseja encontrar")    

        

        try:
            colunas = ["Material","Texto breve material","Utilização livre"]
            leitor_sap  = pd.read_excel(df,usecols=colunas)
            newleitor = leitor_sap[leitor_sap["Material"].astype(str).str.contains(filtro,case=False,na=False)]
        
        except ValueError:
            st.error("⚠️ A planilha não contém as colunas necessárias.")
            st.info("As colunas esperadas são: Material, Texto breve material e Utilização livre.")
            return
        
        col1,col2 = st.columns(2)

        gb = GridOptionsBuilder.from_dataframe(newleitor)

        gb.configure_default_column(filter=True)

        gridOptions = gb.build()

        with col1:
            
            if not newleitor.empty:
                utilizacao = newleitor["Utilização livre"].iloc[0]
                st.metric("Quantidade de produto",utilizacao)

        agora = datetime.now().strftime("%d/%m/%Y")

        with col2:
            st.metric("Data",agora)

        style_metric_cards(
            background_color="#800080",
            border_left_color="#FBF7F7"
        )

        df = AgGrid(
            newleitor,
            gridOptions = gridOptions,
            height = 300)
    
    else:
        st.warning("Selecione a planilha que deseja visualizar")

    

    