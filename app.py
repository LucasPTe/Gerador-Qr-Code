import qrcode
import streamlit as st
st.header('Criador de QrCode')

qr_gerado = False   
def renderizar_qrcode():
    st.image('qrcodes/qrcode.png')

with st.form("Criacao_qrcode"):
    link = st.text_input('Insira o link que deseja transformar em QrCode')
    criar_qrcode = st.form_submit_button("Criar QrCode")
    if criar_qrcode:
        qr = qrcode.make(link)
        qr.save("qrcodes/qrcode.png")
        st.success('Qr Code criado com sucesso!')
        renderizar_qrcode()
        qr_gerado = True
        with open("qrcodes/qrcode.png", "rb") as img_file:
            img_bytes = img_file.read()

if qr_gerado == True:
    st.download_button(label='Baixar QRCode',data = img_bytes, file_name="qrcode.png")