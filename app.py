import streamlit as st

st.set_page_config(page_title="Nutri Amorim", page_icon="images/favicon.ico", layout="wide")

st.markdown(
    """
    <style>
        .stApp {
            background-color: #2E8B57; /* Verde-mar */
        }
         .stSidebar {
            background-color:  #2E8B57; /* Verde-mata para a barra lateral */
            border-right: 2px solid #FFFFFF; /* Borda branca separando a barra lateral do conteúdo */
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Nutri Amorim - Seu Blog de Nutrição")

st.sidebar.title("Menu")
page = st.sidebar.radio("Navegue pelo site", ["Início", "Sobre", "Receitas", "Pesquisas"])

if page == "Início":
    st.header("Bem-vindo ao Blog Nutri Amorim!")
    st.write("Aqui você encontrará conteúdos sobre nutrição, pesquisas científicas e receitas saudáveis.")

elif page == "Sobre":
    st.header("Sobre o Blog")
    st.write("Este blog foi criado para compartilhar conhecimento sobre alimentação saudável e nutrição baseada em evidências.")

elif page == "Receitas":
    st.header("Receitas Saudáveis")
    st.write("Em breve, receitas deliciosas para uma vida mais saudável!")

elif page == "Pesquisas":
    st.header("Pesquisas Científicas")
    st.write("Confira estudos e artigos científicos sobre nutrição.")

st.markdown("---")
st.write("© 2025 Nutri Amorim - Todos os direitos reservados")