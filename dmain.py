import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import os

# 대화기록 남기기
def add_to_conversation_user(prompt):
    st.session_state.conversation_history.append(("당신: ", prompt))
def add_to_conversation_gpt(response):
    st.session_state.conversation_history.append(("찰리: ", response))

def send_click(i):
    
    if i==0: return "안녕하세요, 오랜만이에요. 어떤 주제로 대화를 나누면 좋을까요?"
    elif i==1: return "좋아요, 같이 이야기 해 봐요. 어떤 음식을 가장 좋아하시나요?"
    elif i==2: return "피자를 가장 좋아하시는군요. 그 이유가 뭔가요?"
    elif i==3: return "그렇군요. 다양한 맛을 즐길 수 있다는 것은 매력적이죠. 어떤 토핑을 가장 좋아하시나요?"
    elif i==4: return "감자 토핑을 가장 좋아하시는군요. 감자 맛있죠. 피자를 좋아하는 다른 이유도 있나요?"
    elif i==5: return "그렇죠, 피자는 혼자 먹기 어렵죠. 그리고 함께 먹으면 더 즐거워요. "
    elif i==6: return "즐거운 경험이었겠군요. 친구와 어벤져스를 보면서 먹은 피자는 더 맛있었을 것 같아요. 다음에는 어떤 영화를 보며 피자를 먹을 건가요?"
    elif i==7: return "알겠어요. 좋아하는 장르가 있으신가요?"
    elif i==8: return "액션영화를 좋아하시는군요. '미션임파서블' 시리즈 어떠신가요? 혹시 이미 보신 적이 있나요?"
    elif i==9: return "그렇군요. 그렇다면 '범죄도시' 시리즈 어떠신가요?"
    else : return "다행이네요. 친구와 함께 영화를 보면서 즐거운 시간을 보내시길 바라요."
    


# Streamlit 앱 생성
def main():
    st.subheader("대화하기")      # Streamlit 앱 제목 설정
    st.session_state.conversation_history = []
    greeting="안녕하세요, 찰리입니다. 편하게 말 걸어 주세요."
    add_to_conversation_gpt(greeting)
    
    for i in range(11):
        user_input = st.text_input("유저: ", key=f'{i}')
        if st.button("보내기"):
            add_to_conversation_user(user_input)
            response = send_click(i)
            add_to_conversation_gpt(response)    # 응답을 출력하는 서브헤더와 성공 메시지 위젯 생성
    
    
 # 역순으로 대화기록 출력
    for role, message in reversed(st.session_state.conversation_history):
        st.write(f"{role} {message}")
 
if __name__ == '__main__':
    main()
