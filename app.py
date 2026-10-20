import streamlit as st

st.set_page_config(page_title="Dashboard ADEM", layout="centered")
st.title("📊 Cálculo de Notas")

adem = st.slider("Nota ADEM", 0.0, 10.0, 7.0, 0.1)
app = st.slider("Nota APP",0.0, 10.0, 7.0, 0.1)
af = st.slider("Nota AF", 0.0, 10.0, 7.0, 0.1)
meaif = st.slider("Nota MEAIF", 0.0, 10.0, 7.0, 0.1)
ps = st.slider("Nota PS", 0.0, 10.0, 7.0, 0.1)
olv = st.slider("Nota OLV", 0, 2, 0)

media = (((4*adem) + (2*app) + (2*af) + meaif + ps)/10) + olv
if media > 10:
  st.subheader(f"Sua média é maior que 10, é {media:.2f}")
elif 10 >= media >= 7:
  st.subheader(f"Sua média é {media:.2f}, sua nota está na média")
else:
  st.subheader(f"Sua média é {media:.2f}, sua nota está abaixo da média")