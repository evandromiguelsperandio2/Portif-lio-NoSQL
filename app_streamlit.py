import streamlit as st
from pymongo import MongoClient

client = MongoClient("mongodb+srv://internaltamiguel123_db_user:jJBdVvezx7QMcINw@cluster0.k1uh9ix.mongodb.net/?appName=Cluster0")
db = client['meu_banco']
colecao = db['usuarios']

st.title('Usuários cadastrados')
dados = list(colecao.find({}, {'_id': 0}))
st.table(dados)