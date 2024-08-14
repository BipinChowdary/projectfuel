import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="My Homepage", page_icon='🏡', layout="wide")
st.markdown('<style>div.block-container{padding-top:2.5rem;}</style>', unsafe_allow_html=True)

def load_font(font_path):
    with open(font_path, "rb") as font_file:
        font_data = font_file.read()
    encoded_font = base64.b64encode(font_data).decode('utf-8')
    return encoded_font

# Load custom font
tech_font = load_font('fonts/TECH.ttf')

# Define custom CSS
custom_css = f"""
<style>
@font-face {{
    font-family: 'TechFont';
    src: url(data:font/ttf;base64,{tech_font}) format('truetype');
}}
.title {{
    font-family: 'TechFont', sans-serif;
    font-size: 3rem;
    margin: 0;
    padding: 0;
    margin-bottom: 2rem;
}}
.gradient-divider {{
    height: 3px;
    background: linear-gradient(to right, red, purple);
    border: none;
    margin-top: -20px;
    margin-bottom: 20px;
}}
</style>
"""

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown('<h1 class="title">🏡 Fuel Efficiency Prediction</h1>', unsafe_allow_html=True)

st.write(' ')

# Define columns for layout
col1, _, col2 = st.columns([4, 0.5, 5.5])

with col1:
    with open('images/header.png', 'rb') as f:
        image = f.read()
    st.image(image, width=500)

col2.markdown('<h4 class="title2">Why Fuel Efficiency Prediction Is Useful?</h4><p class="gradient-divider"></p>', unsafe_allow_html=True)
col2.write('Fuel efficiency prediction contributes significantly to pollution reduction by promoting the adoption of cleaner and more sustainable transportation options. By accurately forecasting fuel consumption, our project empowers individuals and businesses to make informed decisions that prioritize vehicles with lower emissions and higher fuel efficiency ratings. Moreover, our fuel efficiency prediction project facilitates the development and deployment of innovative technologies aimed at enhancing vehicle performance while minimizing environmental impact. Ultimately, our efforts in fuel efficiency prediction contribute to a cleaner, healthier planet for present and future generations.')

# Single button to open a URL
st.write(" ")
if st.button("🔗 Open Project Page"):
    st.markdown("[Click here to visit the project page](https://projectfuel.github.io)")
