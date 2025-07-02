# Only used in local
# The real values stored in github secrets

# from dotenv import load_dotenv
# load_dotenv()


from langchain_openai import OpenAI, ChatOpenAI

llm = OpenAI()
chat_model = ChatOpenAI()



import streamlit as st

st.title("AI Poet")

title = st.text_input("시의 주제를 입력하세요")


st.write("주제:", title)  


if st.button("시를 써 줘!"):
    if not title:
        st.error("주제를 입력해주세요.")
    else:
        with st.spinner("시를 작성하는 중입니다..."):

          result=chat_model.invoke(title + "에 관한 시를 지어줘.")

          st.write(result.content)

          st.write("시 작성 완료!")


          