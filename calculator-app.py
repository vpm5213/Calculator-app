import streamlit as st
import datetime
import base64

st.set_page_config(layout="wide")

def get_base64_image(path):
  with open(path, 'rb') as f:
    return base64.b64encode(f.read()).decode()
today = datetime.date.today()

bg_image = get_base64_image("assets/image.png")
st.markdown(f"""
<style>
    .stApp{{
            background-image:url("data:image/png;base64,{bg_image}");    
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
    }}
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) {{
        background-color: transparent; 
    }}
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) {{
        background-color: blue; 
        padding: 20px;
        border-radius: 10px;
    }}
    div[data-testid="stHorizontalBlock"] > div:nth-child(3) {{
        background-color: transparent; /* Makes col3 invisible */
    }}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1], border=False)

with col2:
  st.markdown("<h1 style='text-align: justify;'>DOB Calculator</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='text-align: justify;'>Enter your age:</h3>", unsafe_allow_html=True)
    
  DOB = st.date_input('', min_value=datetime.date(1947, 8, 15),max_value=today)
  
age = (today-DOB).days//365
st.markdown(f"Your current age is: {age}", unsafe_allow_html=True, text_alignment="center")

