import streamlit as st
import google.generativeai as genai
import os

# 1. Habaynta Muuqaalka (Branding & Colors)
st.set_page_config(page_title="Humanity-First Marketplace", page_icon="🌍", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 25px; background-color: #007bff; color: white; height: 3em; font-size: 20px; }
    .impact-card { background-color: #ffffff; padding: 20px; border-radius: 15px; border-left: 10px solid #28a745; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    .business-header { color: #1e3a8a; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. Xiriirka AI-ga
api_key = os.environ.get("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Cillad: GOOGLE_API_KEY laguma helin 'Secrets'.")

# 3. Header-ka App-ka
st.title("🌍 Humanity-First Platform")
st.markdown("<h3 style='color: #4b5563;'>German Marketplace for Cars & Housing</h3>", unsafe_allow_html=True)
st.info("Hadafkeenu waa: 'Nothing is greater than humanity. Hunger is the key to conflict.'")

# 4. Marketplace - Qaybaha Guryaha iyo Baabuurta
tab1, tab2 = st.tabs(["🏠 Real Estate (Housing)", "🚗 Automotive (Cars)"])

with tab1:
    st.subheader("Property Selection")
    col1, col2 = st.columns(2)
    with col1:
        re_city = st.selectbox("Location (Germany)", ["Hamburg", "Berlin", "Munich", "Frankfurt", "Stuttgart"])
        re_type = st.radio("Type", ["Buy", "Rent"])
    with col2:
        re_price = st.number_input("Property Price/Rent (€)", min_value=500, value=250000, step=1000)
    re_desc = st.text_area("Property Details", "e.g. 3-bedroom apartment near the lake.")

with tab2:
    st.subheader("Vehicle Selection")
    col3, col4 = st.columns(2)
    with col3:
        car_brand = st.selectbox("Brand", ["BMW", "Mercedes-Benz", "Volkswagen", "Audi", "Tesla", "Porsche"])
        car_model = st.text_input("Model Details", "e.g. 2024 Electric Sedan")
    with col4:
        car_price = st.number_input("Car Price (€)", min_value=1000, value=45000, step=500)
    car_desc = st.text_area("Vehicle Condition", "e.g. New condition, full service history.")

# 5. Xisaabinta iyo Saamaynta (The Heart of the App)
st.divider()
if st.button("Analyze Deal & Calculate Humanity Impact ➔"):
    # Go'aami qiimaha la falanqaynayo
    final_price = re_price if tab1 else car_price
    item_name = f"{re_type} in {re_city}" if tab1 else f"{car_brand} {car_model}"
    
    # Impact Math
    donation = final_price * 0.05
    meals = int(donation / 2) # €2 halkii cunto
    
    with st.spinner("AI is analyzing the business value and humanitarian impact..."):
        # AI Analysis
        prompt = f"""
        You are a professional AI Assistant for the German {item_name} market. 
        1. Analyze this deal at {final_price} EUR and explain its business potential.
        2. Explain how a 5% donation ({donation} EUR) will provide {meals} meals to fight global hunger.
        3. Use a tone of peace, dignity, and love. Quote: 'When the stomach is empty, the mind goes silent.'
        """
        response = model.generate_content(prompt)
        
        # Bandhigga Natiijada
        st.success("Analysis Complete!")
        
        c1, c2 = st.columns([2, 1])
        with c1:
            st.markdown(f"### 🤖 AI Business Insight\n{response.text}")
        
        with c2:
            st.markdown(f"""
                <div class="impact-card">
                    <h3 style="color: #28a745;">🌍 Impact Dashboard</h3>
                    <p>Transaction: <b>€{final_price:,.2f}</b></p>
                    <hr>
                    <p>Humanitarian Donation (5%):</p>
                    <h2 style="color: #28a745;">€{donation:,.2f}</h2>
                    <p>Meals for the Hungry:</p>
                    <h1 style="color: #28a745;">{meals:,}</h1>
                    <p><i>Every deal saves lives.</i></p>
                </div>
            """, unsafe_allow_html=True)
            st.balloons()
