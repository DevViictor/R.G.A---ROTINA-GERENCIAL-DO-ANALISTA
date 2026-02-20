import streamlit as st 
import pandas as pd
from db.banco import conexao
from zoneinfo import ZoneInfo
from datetime import datetime
from streamlit_extras.colored_header import colored_header
from st_aggrid import AgGrid,GridOptionsBuilder

def visualizar_iguatemi1():

    st.set_page_config(page_title="R.G.A - ATRIBUIÇÕES",layout="wide")
    
    def visualizar_tarefa():

        conn = conexao()

        tabela = "SELECT * FROM tarefas"

        df = pd.read_sql(tabela,conn)
        conn.close()
        return df    

    df = visualizar_tarefa()

    df["data"] = pd.to_datetime(df["data"])


    colored_header(
        label="R.G.A - Atribuições",
        description="Suas tarefas diárias",
        color_name="orange-70"
    )


    col1,col2 = st.columns(2)

    with col1:
        op = st.selectbox(
            "Seleção",[
                "Tarefas",
                "Concluidas"
            ]
        )

    if op == "Tarefas":

        with col2:
            data_selecionada = st.date_input(
            "Data da tarefa",
            value=datetime.now().date()
            )
            
        df_loja = df[
        (df["loja"] == "IGUATEMI |") &
        (df["data"].dt.date == data_selecionada)
        ].copy()

        if df_loja.empty:
            st.info("Nenhuma tarefa adicionada")
        
        
        df_loja["observacao"] = ""
        df_loja["concluir"] = False

        gb = GridOptionsBuilder.from_dataframe(df_loja)


        gb.configure_column(
            "concluir",
            editable= True,
            cellRenderer="agCheckboxCellRenderer",
            cellEditor="agCheckboxCellEditor"
        )

        gridOptions = gb.build()
                    
        editado = AgGrid(
            df_loja,
            fit_columns_on_grid_load=True,
            gridOptions=gridOptions,
            update_mode="SELECTION_CHANGED",
            domLayout='autoHeight',
            height=300
        )

        df_editado = editado["data"]
            
        if st.button("Registrar"):
            
            concluidos  = df_editado[df_editado["concluir"] == True]

            for _,linha in concluidos.iterrows():

                FUSO_BR = ZoneInfo("America/Sao_Paulo")

                agora = datetime.now(FUSO_BR)

                data_atual = agora.date()
                hora_atual = agora.time().replace(microsecond=0)

                
                conn = conexao()
                cursor = conn.cursor()

                cursor.execute("""

                INSERT INTO registro(
                            tarefa,
                            analista,
                            data,
                            hora,
                            observacao) VALUES(%s,%s,%s,%s,%s)
                            ON CONFLICT ON CONSTRAINT unique_registro DO NOTHING

                                
                """, (
                    linha["titulo"],
                    "IGUATEMI |",
                    data_atual,
                    hora_atual,
                    linha["observacao"]
                    ))
                
                conn.commit()
                conn.close()

            st.success("Tarefas registradas com sucesso!")
        

    if op == "Concluidas":
    
        st.set_page_config("Tarefas conluidas",layout="wide")

        def visualizar_registro():

            conn = conexao()

            sql = "SELECT * FROM registro"

            df = pd.read_sql(sql,conn)

            return df
        
        registro = visualizar_registro()
        
        registro["data"] = pd.to_datetime(registro["data"])


        with col2:

            data_selecionada = st.date_input(
            "Data da tarefa",
            value=datetime.now().date()
            )

        registro_perido = registro[
        (registro["data"].dt.date == data_selecionada)
        ].copy()

        if registro_perido.empty:
            st.info("Nenhuma tarefa concluida")

        gb = GridOptionsBuilder.from_dataframe(registro_perido)
        
        gridOptions = gb.build()

        AgGrid(registro_perido,
            fit_columns_on_grid_load=True,
            gridOptions=gridOptions,
            domLayout='autoHeight'
                )