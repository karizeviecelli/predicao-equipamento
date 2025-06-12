import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Predição de Equipamento", layout="centered")

# Título
st.title("🔧 Predição de Equipamentos Industriais")
st.write("Este app prevê o **preço estimado** com base nas características do equipamento.")

# Entradas do usuário
st.header("📥 Insira os dados do equipamento")

potencia = st.slider("Potência (kW)", 0, 1000, 200)
durabilidade = st.slider("Durabilidade (anos)", 0, 20, 5)
tecnologia = st.slider("Tecnologia embarcada (0-10)", 0, 10, 5)
peso = st.number_input("Peso (kg)", min_value=0.0, value=50.0)

necessidade_energia = st.selectbox("Necessidade de energia especial?", ["Sim", "Não"])
manutencao = st.selectbox("Requer manutenção?", ["Sim", "Não"])
iot = st.selectbox("Possui IoT?", ["Sim", "Não"])
protecao_corrente = st.selectbox("Tem proteção contra corrente?", ["Sim", "Não"])
sistema_refri = st.selectbox("Sistema de refrigeração incluso?", ["Sim", "Não"])
garantia = st.selectbox("Possui garantia estendida?", ["Sim", "Não"])
com_software = st.selectbox("Acompanha software?", ["Sim", "Não"])

# Criar DataFrame com as entradas normalizadas
entrada = pd.DataFrame([[
    potencia / 1000,
    durabilidade / 20,
    tecnologia / 10,
    peso / 200,
    1 if necessidade_energia == "Sim" else 0,
    1 if manutencao == "Sim" else 0,
    1 if iot == "Sim" else 0,
    1 if protecao_corrente == "Sim" else 0,
    1 if sistema_refri == "Sim" else 0,
    1 if garantia == "Sim" else 0,
    1 if com_software == "Sim" else 0
]], columns=['potencia', 'durabilidade', 'tecnologia', 'peso', 'necessidade_energia', 'requere_manutencao', 'iot', 'protecao_corrente', 'sistema_refri', 'garantia', 'com_software'])

# Botão de previsão
if st.button("🔍 Prever preço"):
    try:
        modelo = joblib.load("modelo_preco.pkl")
        preco_previsto = modelo.predict(entrada)
        st.success(f"💰 Preço previsto: R$ {preco_previsto[0]:,.2f}")
    except Exception as e:
        st.error(f"❌ Erro ao fazer a previsão: {str(e)}")
