import streamlit as st

st.title("Echo Bot")

# Sohbet geçmişi
if "messages" not in st.session_state:
    st.session_state.messages = []

# Uygulama yeniden çalıştırıldığında geçmişteki sohbet mesajlarını görüntüleme
for message in st.session_state.messages:
    with st.chat_message(message["role"],avatar=message["avatar"]):
        st.markdown(message["content"])

# Kullanıcı girdisine tepki verme
if prompt := st.chat_input("Metin girin"):
    user_avatar = "🙂"
    # Sohbet mesajı konteynerinde kullanıcı mesajını görüntüleme
    st.chat_message("user",avatar=user_avatar).markdown(prompt)
    # Sohbet geçmişine kullanıcı mesajı ekleme
    st.session_state.messages.append({"role": "user", "content": prompt,"avatar": user_avatar})

    response = f"Echo: {prompt}"
    assistant_avatar = "🦜"
    # Sohbet mesajı konteynerinde bot yanıtını görüntüleme
    with st.chat_message("assistant",avatar=assistant_avatar):
        st.markdown(response)
    # Sohbet geçmişine bot yanıtı ekleme
    st.session_state.messages.append({"role": "assistant", "content": response,"avatar": assistant_avatar})