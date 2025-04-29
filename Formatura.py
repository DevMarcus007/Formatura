import streamlit as st
from datetime import date

# Datas
hoje = date.today()
data_inicio = date(2025, 1, 1)
data_formatura = date(2025, 12, 20)

# Cálculos
total_dias = (data_formatura - data_inicio).days
dias_passados = (hoje - data_inicio).days
dias_faltando = (data_formatura - hoje).days
percentual = max(0, min(100, int((dias_passados / total_dias) * 100)))

# Título
col1, col2, col3 = st.columns([2,1,2])
with col2:
    st.image("diploma.webp", width=200,)

st.title(f"Formatura OESM 2025 - Turma 502")

st.markdown(f"<p style='text-align: center;  padding: 1px; font-size: 32px;'>Faltam {dias_faltando} dias.</p>", unsafe_allow_html=True)

# Barra de progresso personalizada horizontal
barra_html = f"""
<div style="width: 100%; max-width: 700px; height: 60px; border: 2px solid #aaa; background-color: #f0f0f0; position: relative; border-radius: 10px; overflow: hidden; margin-top: 30px;">
    <div style="width: {percentual}%; height: 100%; background-color: #4CAF50;"></div>
</div>
<p style="text-align: center; font-weight: bold; margin-top: 10px;">{percentual}% concluído</p>
"""

st.markdown(barra_html, unsafe_allow_html=True)



imagens = [
    "foto1.jpg",
    "foto2.webp",
    "foto3.webp"
]

# Controle de índice usando estado da sessão
if "indice" not in st.session_state:
    st.session_state.indice = 0

# Funções para navegação
def proximo():
    st.session_state.indice = (st.session_state.indice + 1) % len(imagens)

def anterior():
    st.session_state.indice = (st.session_state.indice - 1) % len(imagens)

# Botões de navegação
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.button("⬅️ Anterior", on_click=anterior)
with col3:
    st.button("Próximo ➡️", on_click=proximo)

# Exibição da imagem atual
st.image(imagens[st.session_state.indice], use_column_width=True)
