
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
iot = st.selectbox("Possui IoT?", ["Sim", "Não"])
manutencao = st.selectbox("Requer manutenção?", ["Sim", "Não"])
tecnologia = st.slider("Tecnologia embarcada (0-10)", 0, 10, 5)
peso = st.number_input("Peso (kg)", min_value=0.0, value=50.0)

# Criar DataFrame com as entradas normalizadas
entrada = pd.DataFrame([{
    'potencia': potencia / 1000,
    'durabilidade': durabilidade / 20,
    'iot': 1 if iot == "Sim" else 0,
    'requere_manutencao': 1 if manutencao == "Sim" else 0,
    'tecnologia': tecnologia / 10,
    'peso': peso / 200
}])

# Botão de previsão
if st.button("🔍 Prever preço"):
    try:
        modelo = joblib.load("modelo_preco.pkl")
        preco_previsto = modelo.predict(entrada)
        st.success(f"💰 Preço previsto: R$ {preco_previsto[0]:,.2f}")
    except FileNotFoundError:
        st.error("❌ Arquivo 'modelo_preco.pkl' não encontrado. Gere o modelo no notebook e tente novamente.")
