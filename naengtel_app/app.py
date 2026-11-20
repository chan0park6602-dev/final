"""냉털메이트 실행 파일.

실행:  streamlit run app.py
첫 화면은 랜딩페이지 없이 바로 '재고 관리(내 냉장고)'로 들어간다 (명세서 27번).
"""
import streamlit as st

st.set_page_config(page_title="냉털메이트", page_icon="🧊", layout="wide")
st.switch_page("pages/1_fridge.py")
