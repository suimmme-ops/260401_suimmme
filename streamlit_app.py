import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Streamlit 요소 샘플", layout="wide")

st.title("🎉 Streamlit UI 요소 데모")
st.markdown("Streamlit에서 사용할 수 있는 대표적인 UI 컴포넌트를 보여주는 예제 페이지입니다.")

st.header("1. 텍스트")
st.subheader("1-1. 다양한 텍스트")
st.write("일반 텍스트 출력: Hello Streamlit!")
st.caption("캡션 텍스트")
st.code("print('Hello, world!')", language='python')

st.header("2. 입력 위젯")
col1, col2, col3 = st.columns(3)
with col1:
    text_input = st.text_input("텍스트 입력", "여기에 입력하세요")
    number_input = st.number_input("숫자 입력", min_value=0, max_value=100, value=10)
with col2:
    date_input = st.date_input("날짜 선택")
    checkbox = st.checkbox("체크박스")
with col3:
    selectbox = st.selectbox("선택 상자", ["옵션 A", "옵션 B", "옵션 C"])
    multiselect = st.multiselect("다중 선택", ["사과", "바나나", "체리"], default=["사과"])

st.write("입력 결과:", text_input, number_input, date_input, checkbox, selectbox, multiselect)

st.header("3. 버튼 및 액션")
if st.button("클릭하세요"):
    st.success("버튼을 눌렀습니다!")

if st.button("경고 버튼"):
    st.warning("주의: 버튼이 눌렸습니다.")

st.header("4. 레이아웃")
with st.expander("추가 정보 숨기기/보이기"):
    st.write("확장 가능한 패널 내부의 텍스트입니다.")

st.echo("with st.echo(): 코드 + 실행 결과 동시 표시")

st.header("5. 표와 데이터")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.dataframe(chart_data)
st.table(chart_data.head())
st.line_chart(chart_data)
st.bar_chart(chart_data)

st.header("6. 미디어")
st.image("https://static.streamlit.io/examples/dog.jpg", caption="강아지 이미지 예시", use_column_width=True)
st.audio("https://www2.cs.uic.edu/~i101/SoundFiles/BabyElephantWalk60.wav")
st.video("https://www.youtube.com/watch?v=JwYX52BP2Sk")

st.header("7. 사이드바")
with st.sidebar:
    st.title("사이드바")
    st.write("사이드바에서 설정합니다.")
    sidebar_slider = st.slider("슬라이더", min_value=0, max_value=100, value=25)

st.write("사이드바 슬라이더 값:", sidebar_slider)

st.header("8. 상태 표시")
with st.spinner("로딩중..."):
    import time
    time.sleep(0.2)
st.success("로드 완료!")
