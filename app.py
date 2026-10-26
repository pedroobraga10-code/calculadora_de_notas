import streamlit as st

st.set_page_config(page_title="Média Escolar Espaço Aberto", layout = "wide")

#Aplica estilos CSS à página utilizando HTML
st.markdown("""
<!-- Controle da aparência da página -->
<style>
    
     /* Seleciona o contêiner principal do conteúdo da página */
    .block-container {

        /* 1rem = tamanho da fonte raiz (geralmente 16px) */
        
        /* Controla o espaçamento superior da página */
        padding-top: 4rem;
        
        /* Controla o espaçamento inferior da página */
        padding-bottom: 0.5rem;
    }

    /* Seleciona os contêineres verticais do Streamlit */
    div[data-testid="stVerticalBlock"] {
        /* Controla o espaçamento entre os elementos dentro de cada contêiner vertical */
        gap: 0.4rem;
    }
</style>
""", unsafe_allow_html=True)

# Logo e título na mesma linha com título centralizado
logo, titulo, espaco = st.columns([1, 8, 1], vertical_alignment="center")

with logo:
    st.image("logo_colegio.png", width=90)

with titulo:
    #Exibe conteúdo formatado em Markdown ou HTML
    st.markdown(
        #Alinhamento do texto,          título
        "<h1 style='text-align: center;'>Cálculo de Notas</h1>",
        unsafe_allow_html=True
    )

col1, col2 = st.columns([2, 1], gap = "small")

with col1:
    adem = st.slider("Nota ADEM", 0.0, 10.0, 7.0, 0.1)

    app = st.slider("Nota APP",0.0, 10.0, 7.0, 0.1)

    af = st.slider("Nota AF (Trabalho Bimestral) ", 0.0, 10.0, 7.0, 0.1)

    meaif = st.slider("Nota MEAIF (Trilha)", 0.0, 10.0, 7.0, 0.1)

    ps = st.slider("Nota PS", 0.0, 10.0, 7.0, 0.1)

    olv = st.slider("Nota OLV (Olimpíadas e Vestibulares)", 0.0, 2.0, 0.0, 0.5)

media = (((4*adem) + (2*app) + (2*af) + meaif + ps)/10) + olv

with col2:

    # Espaço superior para alinhamento
    st.markdown("<div style='padding-top: 80px;'></div>", unsafe_allow_html=True)

    #Exibe conteúdo formatado em Markdown ou HTML
    st.markdown(
        #Alinhamento do texto,      tamanho da fonte,    título
        "<h1 style='text-align: center; font-size: 40px;'>Nota:</h1>",
        unsafe_allow_html=True
    )

    if media >= 7:
        #Exibe conteúdo formatado em Markdown ou HTML
        st.markdown(
            #Alinhamento do texto,   cor da nota,   tamanho da fonte,  nota
            f"<h1 style='text-align: center; color: #00C853; font-size: 60px;'>{media:.2f}</h1>",
            unsafe_allow_html=True
        )

        #Exibe conteúdo formatado em Markdown ou HTML
        st.markdown(
            #Alinhamento do texto,           frase sobre a nota
            "<h3 style='text-align: center;'>Nota na média</h3>",
            unsafe_allow_html=True
        )

    else:
        #Exibe conteúdo formatado em Markdown ou HTML
        st.markdown(
            #Alinhamento do texto,           cor da nota,   tamanho da fonte,  nota
            f"<h1 style='text-align: center; color: #FF1744; font-size: 60px;'>{media:.2f}</h1>",
            unsafe_allow_html=True
        )

        #Exibe conteúdo formatado em Markdown ou HTML
        st.markdown(
            #Alinhamento do texto,           frase sobre a nota
            "<h3 style='text-align: center;'>Nota abaixo da média</h3>",
            unsafe_allow_html=True
        )