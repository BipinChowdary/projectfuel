import streamlit as st

# Set page configuration
st.set_page_config(page_title="My Homepage", page_icon='🏡', layout="wide")
st.markdown('<style>div.block-container{padding-top:2.5rem;}</style>', unsafe_allow_html=True)

# Page title
st.markdown('<h1 style="font-size: 3rem;">🏡 Fuel Efficiency Prediction</h1>', unsafe_allow_html=True)

st.write(' ')

# Define columns for layout
col1, _, col2 = st.columns([4, 0.5, 5.5])

with col1:
    with open('images/header.png', 'rb') as f:
        image = f.read()
    st.image(image, width=500)

col2.markdown('<h4 style="font-size: 1.8rem;">Why Fuel Efficiency Prediction Is Useful?</h4>', unsafe_allow_html=True)
col2.write('Fuel efficiency prediction contributes significantly to pollution reduction by promoting the adoption of cleaner and more sustainable transportation options. By accurately forecasting fuel consumption, our project empowers individuals and businesses to make informed decisions that prioritize vehicles with lower emissions and higher fuel efficiency ratings. Moreover, our fuel efficiency prediction project facilitates the development and deployment of innovative technologies aimed at enhancing vehicle performance while minimizing environmental impact. Ultimately, our efforts in fuel efficiency prediction contribute to a cleaner, healthier planet for present and future generations.')

# Natural Streamlit buttons
if st.button("💻 Open Project Code"):
    st.write("[Click here to visit the Project Code](https://github.com/your_project_repo)")

if st.button("🌐 Visit My Portfolio"):
    st.write("[Click here to visit My Portfolio](https://yourportfolio.com)")
