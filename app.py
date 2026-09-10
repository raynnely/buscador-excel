import streamlit as st
import pandas as pd

st.title("🔎 Buscador de Excel")

st.write("Selecione sua tabela Excel abaixo:")

arquivo = st.file_uploader(
    "Escolha um arquivo Excel",
    type=["xlsx"],
    key="excel_upload"
)

if arquivo is not None:

    tabela = pd.read_excel(arquivo)

    st.subheader("🔎 Pesquisar")

    palavra = st.text_input(
        "Digite uma ou mais palavras para pesquisar:"
    )

    if palavra:

        tabela_busca = tabela.astype(str)

        palavras = palavra.split()

        resultado = tabela[
            tabela_busca.apply(
                lambda linha: all(
                    linha.str.contains(
                        termo,
                        case=False,
                        na=False
                    ).any()
                    for termo in palavras
                ),
                axis=1
            )
        ]

        st.subheader("🔎 Resultado da busca")

        if len(resultado) > 0:

            st.success(
                f"{len(resultado)} resultado(s) encontrado(s)."
            )

            st.dataframe(
                resultado,
                use_container_width=True
            )

        else:

            st.warning(
                "Nenhum resultado encontrado."
            )
            