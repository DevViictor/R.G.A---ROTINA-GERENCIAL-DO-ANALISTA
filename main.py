import streamlit as st
from Tarefas.Criar import tarefas_iguatemi
from Tarefas.Visualizar import visualizar_iguatemi1
from Contagem.AuxilarEstoque import contagem
from streamlit_option_menu import option_menu
from Contagem.attach import registro_attach

with st.sidebar:
    op = option_menu(
        "Menu",
        ["Criação",
         "Tarefas",
         "Estoque",
         "Attach"],
        icons = ["card-list","clipboard-data","clipboard-check-fill","tablet-fill"],
        menu_icon="cast",
        default_index = 0,
        styles = {
            "container": {
                 "background-color": "#310327ff"
            }
        }
    )

 
    if op == "Attach":
        sub_menu = option_menu("ATTACH",
                               ["Registrar","Relátorio"],
                               icons = ["tablet-fill"],
        menu_icon="cast",
        default_index = 0,
        styles = {
            "container": {
                 "background-color": "#310327ff"
            }
        }
    )
        
    
if op == "Criação":
    tarefas_iguatemi()

if op == "Tarefas":
    visualizar_iguatemi1()

if op =="Estoque":
    contagem()

if sub_menu == "Registrar":
    registro_attach()
