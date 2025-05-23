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


from streamlit_carousel import carousel

image_urls = [
    {"title": "", "img": "foto1.jpg", "text": ""},
    {"title": "", "img": "foto2.webp", "text": ""},
    {"title": "", "img": "foto3.webp", "text": ""},
]

carousel(items=image_urls, 
         fade=True, 
         interval=5000, 
         indicators=True,
         wrap = True,
        container_height = 400,
        width = 1)
