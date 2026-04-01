import streamlit as st
import datetime

st.set_page_config(page_title="나의 프로필", layout="wide", page_icon="👤")

st.title("👤 나의 프로필 웹앱")
st.markdown("안녕하세요! 아래 정보를 통해 간단한 자기소개와 주요 역량을 보여주는 프로필 앱입니다.")

# 사이드바 설정
with st.sidebar:
    st.header("설정")
    show_contact = st.checkbox("연락처 표시", value=True)
    theme = st.selectbox("테마", ["기본", "미니멀", "컬러풀"])

# 기본 정보 입력
st.header("1. 기본 정보")
col1, col2 = st.columns([1, 2])
with col1:
    avatar_url = st.text_input("프로필 이미지 URL", "dog.png")
    full_name = st.text_input("이름", "박수임")
    job_title = st.text_input("학교", "서울은진초등학교")
    location = st.text_input("위치", "Seoul, Korea")
with col2:
    # 로컬 경로(리포지토리 파일) 또는 URL 처리 (고정 크기 조정)
    from pathlib import Path
    from PIL import Image

    local_path = Path(avatar_url)
    if not local_path.is_absolute():
        local_path = Path.cwd() / local_path

    try:
        if local_path.is_file():
            img = Image.open(local_path)
            st.image(img, caption="프로필 사진", width=200)
        else:
            st.image(avatar_url, caption="프로필 사진", width=200)
    except Exception as e:
        st.error(f"이미지 로드 실패: {e}")
        st.image("https://via.placeholder.com/200", caption="기본 프로필 사진", width=200)

# 소개 및 핵심 역량
st.header("2. 자기소개")
intro = st.text_area("한 줄 소개", "안녕하세용 ʚ₍ᐢ˶ᵔ ᵕ ᵔ˶ꕤᐢ₎ɞ")


st.header("3. 관심사")
skills = st.multiselect("취미", ["공부", "독서", "디지털드로잉", "여행", "런닝", "웹앱", "연구"], default=["공부", "독서", "디지털드로잉", "여행", "런닝", "웹앱","연구"])
 

st.header("4. 경력/프로젝트")
experience = st.text_area("경력 및 프로젝트 요약", "이것저것 항상 무언가를 하고 있어요 곧 책이 나옵니다 ㅎㅎㅎ")


# 연락처
if show_contact:
    st.header("5. 연락처")
    email = st.text_input("이메일", "dpsel7@sen.go.kr")
    phone = st.text_input("전화번호", "010-****-****")
    linkedin = st.text_input("LinkedIn", "https://www.linkedin.com/in/example")
    st.write(f"- 이메일: {email}")
    st.write(f"- 전화번호: {phone}")
    st.write(f"- LinkedIn: {linkedin}")

# 추가 정보 패널
with st.expander("추가 설정 및 잘못된 입력 예시"):
    st.write("여기에 추가적인 정보 또는 경고를 표시할 수 있습니다.")

# 하단 상태 메시지
st.success(f"{full_name}님의 프로필이 준비되었습니다! | 테마: {theme} | 날짜: {datetime.datetime.now().strftime('%Y-%m-%d')}")

