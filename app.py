import streamlit as st

st.set_page_config(
    page_title="Nutri Amorim - Seu Blog de Nutrição",
    page_icon="imagens/favicon.ico" 
)

st.markdown(
    """
    <link rel="apple-touch-icon" sizes="180x180" href="imagens/apple-touch-icon.png">
    <link rel="icon" type="image/x-icon" href="imagens/favicon.ico">  <!-- Favicon principal -->
    <link rel="icon" type="image/png" sizes="32x32" href="imagens/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="imagens/favicon-16x16.png">
    <link rel="manifest" href="imagens/site.webmanifest">

    <style>
        /* Personaliza a barra superior */
        header[data-testid="stHeader"] {
           background-color: #2E8B57; /* Verde-mata */
        }

        /* Personaliza fundo e barra lateral */
        .stApp {
            background-color: #2E8B57; /* Verde-mar */
        }

        .stSidebar {
            background-color: #2E8B57; /* Verde-mata para a barra lateral */
            border-right: 2px solid #000000; /* Linha de separação preta */
        }

        /* Fundo do conteúdo central */
        .stApp {
            background-color: #FFFFFF; /* Fundo branco */
            color: #000000; /* Texto preto */
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Nutri Amorim - Seu Blog de Nutrição")

st.sidebar.title("Menu")
page = st.sidebar.radio("Navegue pelo site", ["Início", "Sobre", "Receitas", "Pesquisas","Quem Somos Nós",])

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

elif page == "Quem Somos Nós":
    st.header("Quem Somos Nós")
    st.write("""
        Olá! Somos o blog Nutri Amorim, dedicado a oferecer conteúdos sobre nutrição saudável, baseada em evidências científicas.
        
        **Sobre o meu trabalho:**  
        Como futuro nutricionista, meu objetivo é proporcionar um estilo de vida saudável e equilibrado para todos, através de informações valiosas sobre alimentação, receitas e dicas de saúde.

        **Quem sou eu:**  
        Sou Marcos Felipe Amorim Mendes, Estudante de Nutrição na UniCesumar com intuito em ajudar as pessoas a adotarem hábitos saudáveis e transformarem suas vidas através da alimentação. Com base em estudos e pesquisas, compartilho conteúdos que vão de receitas a estudos científicos, tudo para promover o bem-estar e a saúde de quem me acompanha.
    """)

st.markdown("---")
st.write("© 2025 Nutri Amorim - Todos os direitos reservados")