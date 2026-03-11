import streamlit as st 
import pandas as pd
from db.banco import enviar_registro_attach
from streamlit_extras.colored_header import colored_header



def registro_attach():

    st.set_page_config(page_title="R.G.A - ANÁLISE DE ATACH",layout="wide")


    colored_header(
        label="R.G.A - Acompanhamento de attach ",
        description="Acompanhamento de attach dos logistas",
        color_name="orange-70"
    )

    consultores = [" ","Anderson","Ana","Debora","David","Lorena","Lene","Rodrigo"]

    op = [" ","Sim","Não"]

    with st.form("forms"):

        nome =st.selectbox("Nome do consultor: ",consultores)

        col1,col2 = st.columns(2)

        with col1 :
            data = st.date_input("Selecione a data:")
            ap = st.selectbox("Vendeu aparelho:",op)
            

        with col2:
            nota = st.text_input("N° da nota: ")
            ac = st.selectbox("Vendeu acessório",op)
            
        registrar = st.form_submit_button("Registrar")
    
    if registrar:
        enviar_registro_attach(
            nome,
            str(ap),
            str(ac),
            data,
            "IGUATEMI |",
            nota
        )

        st.success("Registro realizado!")





