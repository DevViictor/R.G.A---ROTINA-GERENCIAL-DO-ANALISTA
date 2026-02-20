import streamlit as st 
import pandas as pd
from db.banco import enviar_tarefa 
from streamlit_extras.colored_header import colored_header

def tarefas_iguatemi():

    st.set_page_config(page_title="R.G.A",layout="wide")

    colored_header(
        label="ROTINA GERENCIAL DO ANALISTA",
        description="Defina suas tarefas abaixo",
        color_name="orange-70"
    )

    with st.form("Forms"):

        titulo = st.text_input("Titulo da tarefa: ")

        descricao = st.text_input("Descrição da tarefa:")

        periodos = ["Manhã","Tarde"]

        col1,col2 = st.columns(2)

        with col1:
            data= st.date_input("Data de realização: ")

        with col2:
            periodo = st.selectbox("Selecione o periodo",periodos) 
    
        enviar = st.form_submit_button("Enviar")
        if enviar:
            enviar_tarefa(
                titulo,
                descricao,
                str(periodo),
                data,
                "IGUATEMI |"
                
            )
            st.success("Tarefa enviada")