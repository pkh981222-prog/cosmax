import pathlib

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="가위바위보 게임",
    page_icon="✂️",
    layout="centered",
)

# Streamlit 기본 여백/헤더를 최소화해서 원본 HTML 화면이 꽉 차 보이게 함
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 0.5rem;
            padding-bottom: 0.5rem;
            max-width: 720px;
        }
        header[data-testid="stHeader"] {
            background: transparent;
        }
        iframe {
            border: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_PATH = pathlib.Path(__file__).parent / "game.html"
html_code = HTML_PATH.read_text(encoding="utf-8")

# 원본 html/css/js를 그대로 iframe에 렌더링합니다.
# 게임 화면(가위바위보, 사다리타기, 룰렛, 뱀 게임)이 모두 JS로 동작하므로
# 통짜로 임베드하는 것이 원본 동작을 100% 그대로 재현하는 가장 안전한 방법입니다.
components.html(html_code, height=1000, scrolling=True)
