import pandas as pd
import psycopg2
import streamlit as st

def conexao():
    return psycopg2.connect(
        st.secrets["postgres"]["host"]
    )

conn = conexao()


def enviar_tarefa(titulo,descricao,periodo,data,loja):
    
    conn = conexao()
    cursor = conn.cursor()

    sql = """
        INSERT INTO tarefas(
        titulo,
        descricao,
        periodo,
        data,
        loja
        )VALUES(%s,%s,%s,%s,%s)
"""
    cursor.execute(
    sql,(titulo,descricao,periodo,data,loja))
    conn.commit()
    cursor.close()
    conn.close() 

def enviar_registro_attach(nome,ap,ac,data,loja,nota):
    conn = conexao()
    cursor = conn.cursor()

    sql = """
        INSERT INTO attach(
        nome,
        aparelho,
        acessorio,
        data,
        loja,
        nota
        )VALUES(%s,%s,%s,%s,%s,%s)
"""
    cursor.execute(
    sql,(nome,ap,ac,data,loja,nota))
    conn.commit()
    cursor.close()
    conn.close() 
    