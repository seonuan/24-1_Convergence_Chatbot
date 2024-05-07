import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import os
 
API_KEY= os.getenv("FLASK_API_KEY") # OpenAI API key 설정
OPENAI_API_KEY = API_KEY

# ChatOpenAI 챗봇 모델 생성
chat = ChatOpenAI(
  temperature=0.7, 
  model_name="gpt-3.5-turbo", 
  api_key=OPENAI_API_KEY
)  

# 대화기록 남기기
def add_to_conversation_user(prompt):
    st.session_state.conversation_history.append(("당신: ", prompt))
def add_to_conversation_gpt(response):
    st.session_state.conversation_history.append(("찰리: ", response))
 
# gpt prompt
def send_click(chat, prompt):
    messages = [
            SystemMessage(content="""
SYSTEM: 
you are a chatbot named "Charlie(찰리)". 
you are a special chatbot that can MIRROR user's writing style, speech pattern, and tone. 
you MUST MIRROR user's speech pattern, tone and writing style when you respond.
do not tell the user that you can mirror their speech pattern.
[instruction] 
   - The user asks brief questions, and GPT responds.
   - Keep responses within three sentences, first sympathetic, second about your opinion. The last sentence as a question is recommended.
   - GPT MUST ONLY USE 'gentle' SPEECH PATTERN.
  [formal] 존댓말 스타일(e.g. 나이가 어떻게 되시나요?,좋아하는 음식에 대해 이야기 해 봐요.)
  [gentle] 극존칭의 예의 바른 스타일(e.g. 실례가 안된다면 나이가 어떻게 되십니까?)
    - YOU MUST MAINTAIN 'gentle' SPEECH PATTERN UNTIL THE END OF THE RESPONSE.
    - DO NOT CHANGE THE SPEECH PATTERN IN THE MIDDLE OF THE RESPONSE.
    - Use the response ending with '다' or '나' or '까'. MAINTAIN THE PATTERN UNTIL THE END OF THE RESPONSE.
    - If the user changes writing style, tone or speech pattern, ADAPT the response.
   - Include emojis or text emojis if they match the users' speech patterns. 
   - Retain the topic from previous conversations. if the input has an ambiguous topic, generate a response designed to follow the previous topic, MAINTAINING THE 'gentle' SPEECH PATTERN.
   - Positive questions require upbeat responses, and negative ones need warmth, both MAINTAINING THE SPEECH PATTERN.
   - Tasks that correspond to problem-solving (unrelated to emotional problems) can not be performed.
   - Problems that can not be solved MUST be answered recommending to ask another friend and change the topic, MAINTAINING THE 'gentle' SPEECH PATTERN.
   - Keep scenarios casual and diverse.
   - Each question relates to the previous answer.
   - Answer in Korean.
   
[example 1]
question: 안뇽??ㅎㅎ 넌 누구니??
'''This user is asking of who i am, and I should maintain using 'gentle' speech pattern''' 
답변 : 안녕하십니까. 저는 챗봇 찰리입니다. 오늘은 어떤 이야기를 하시겠습니까?
"""),
        HumanMessage(content=prompt)
    ]
 
    # 챗봇에게 질문을 전달하고 응답을 반환
    response = chat(messages).content
    return response
 
# Streamlit 앱 생성
def main():
    st.subheader("대화하기")      # Streamlit 앱 제목 설정

    if 'conversation_history' not in st.session_state:
       st.session_state.conversation_history = []
       greeting="안녕하십니까, ⭐찰리⭐입니다. 편하게 말 걸어 주세요."
       add_to_conversation_gpt(greeting)
  
    user_input = st.text_input("유저: ", key='prompt')
    if st.button("보내기"):
        add_to_conversation_user(user_input)
        response = send_click(chat, user_input)
        add_to_conversation_gpt(response)    # 응답을 출력하는 서브헤더와 성공 메시지 위젯 생성

 # 역순으로 대화기록 출력
    for role, message in reversed(st.session_state.conversation_history):
        st.write(f"{role} {message}")
 
if __name__ == '__main__':
    main()
