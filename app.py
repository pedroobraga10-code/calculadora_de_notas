import streamlit as st

st.set_page_config(page_title="Dashboard Média", layout = "wide")

# Diminui os espaços vazios da página
st.markdown("""
<style>
    .block-container {
        padding-top: 4rem;
        padding-bottom: 0.5rem;
    }

    div[data-testid="stVerticalBlock"] {
        gap: 0.4rem;
    }
</style>
""", unsafe_allow_html=True)

# Logo e título na mesma linha
logo, titulo = st.columns([1, 8], vertical_alignment="center")

with logo:
    st.image("logo_colegio.png", width=90)

with titulo:
    st.title("Cálculo de Notas")

col1, col2 = st.columns([2, 1], gap = "small")

with col1:
 adem = st.slider("Nota ADEM", 0.0, 10.0, 7.0, 0.1)
 app = st.slider("Nota APP",0.0, 10.0, 7.0, 0.1)
 af = st.slider("Nota AF", 0.0, 10.0, 7.0, 0.1)
 meaif = st.slider("Nota MEAIF", 0.0, 10.0, 7.0, 0.1)
 ps = st.slider("Nota PS", 0.0, 10.0, 7.0, 0.1)
 olv = st.slider("Nota OLV", 0, 2, 0)

media = (((4*adem) + (2*app) + (2*af) + meaif + ps)/10) + olv

with col2:
 if media > 10:
   st.subheader(f"Sua média é maior que 10, é {media:.2f}")
 elif 10 >= media >= 7:
   st.subheader(f"Sua média é {media:.2f}, sua nota está na média")
 else:
   st.subheader(f"Sua média é {media:.2f}, sua nota está abaixo da média")