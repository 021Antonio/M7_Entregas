import streamlit as st
from PIL import Image
from rembg import remove

st.title("Remover de Fundo")

def remover_fundo(image, widget):
    bytes_image = Image.open(image)
    output = remove(bytes_image)
    widget.title("Imagem sem Fundo")
    widget.image(output)

image = st.file_uploader("Escolha uma imagem", type=['png', 'jpg', 'jpeg'])

coluna1, coluna2 = st.columns(2)
if image is not None:
    coluna1.title("Imagem Original")
    coluna1.image(image)
    st.button("Remover Fundo", on_click=remover_fundo, args=(image, coluna2))