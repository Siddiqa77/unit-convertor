import os
import time
import streamlit as st
import pygame
from gtts import gTTS

# Initialize pygame
pygame.mixer.init()

# Conversion Factors
types = {
    "Length": {
        "meter": 1, "kilometer": 0.001, "centimeter": 100, "millimeter": 1000, "mile": 0.000621371,
        "yard": 1.09361, "foot": 3.28084, "inch": 39.3701, "nautical mile": 0.000539957, "light year": 1.057e-16
    },
    "Weight": {
        "kilogram": 1, "gram": 1000, "pound": 2.20462, "ounce": 35.274, "ton": 0.001,
        "milligram": 1_000_000, "microgram": 1_000_000_000, "stone": 0.157473
    },
    "Temperature": {
        "celsius": lambda c: c,
        "fahrenheit": lambda c: (c * 9/5) + 32,
        "kelvin": lambda c: c + 273.15,
    },
    "Time": {
        "second": 1, "minute": 1/60, "hour": 1/3600, "day": 1/86400, "week": 1/604800,
        "month": 1/2.628e+6, "year": 1/3.154e+7
    },
    "Volume": {
        "liter": 1, "milliliter": 1000, "cubic meter": 0.001, "cubic centimeter": 1000,
        "gallon": 0.264172, "quart": 1.05669, "pint": 2.11338, "cup": 4.16667
    }
}

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Raleway:wght@500;700&family=Orbitron:wght@500&display=swap');

    /* Global styles */
    body {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #141e30, #243b55) !important;
        color: #ffffff !important;
    }

    /* Main App Container */
    .stApp {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }

   /* Sidebar Styling */
.stSidebar {
    background: linear-gradient(135deg, #1a1a2e, #16213e) !important;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
    
}

/* Sidebar Text Visibility Fix */
.stSidebar div, .stSidebar span, .stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar h4, .stSidebar h5, .stSidebar h6, .stSidebar p {
    color: #0000ff !important;  /* Bright white text for contrast */
    font-family: 'Poppins', sans-serif;
    font-size: 1rem;
    font-weight: 500;
}

/* Sidebar Hover Effects */
.stSidebar div:hover, .stSidebar span:hover, .stSidebar p:hover {
    color: #00ffff !important;  /* Glowing cyan effect on hover */
    text-shadow: 0 0 10px rgba(0, 255, 255, 0.8);
    transition: all 0.3s ease-in-out;
}


    /* Main Title */
    .stTitle {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        font-family: 'Orbitron', sans-serif;
        color: #3c3635 !important;
        text-shadow: 0 0 12px rgba(0, 255, 255, 0.8);
        margin-bottom: 20px;
    }

    /* Subheader */
    .stSubheader {
        font-size: 1.8rem;
        font-weight: bold;
        font-family: 'Raleway', sans-serif;
        color: #ffcc00 !important;
        text-shadow: 0 0 10px rgba(255, 204, 0, 0.8);
    }

    /* Input Fields */
    .stTextInput>div>div>input, 
    .stNumberInput>div>div>input, 
    .stSelectbox>div>div>select {
        background: rgba(255, 255, 255, 0.1) !important;
        color: #ffffff !important;
        border: 2px solid rgba(0, 255, 255, 0.5);
        border-radius: 12px;
        padding: 12px;
        font-size: 1rem;
        font-family: 'Raleway', sans-serif;
        transition: all 0.3s ease;
    }

    /* Glowing Hover Effect */
    .stTextInput>div>div>input:hover, 
    .stNumberInput>div>div>input:hover, 
    .stSelectbox>div>div>select:hover {
        border-color: #00ffff;
        box-shadow: 0 0 12px rgba(0, 255, 255, 0.8);
    }

    /* Button Styling */
    .stButton>button {
        background: linear-gradient(135deg, #ff416c, #ff4b2b) !important;
        color: white !important;
        border: none;
        border-radius: 12px;
        padding: 12px 25px;
        font-size: 1.2rem;
        font-weight: bold;
        font-family: 'Orbitron', sans-serif;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(255, 65, 108, 0.4);
    }

    .stButton>button:hover {
        background: linear-gradient(135deg, #ff4b2b, #ff416c) !important;
        transform: scale(1.05);
        box-shadow: 0 8px 20px rgba(255, 65, 108, 0.6);
    }

    .stButton>button:active {
        transform: scale(0.98);
        box-shadow: 0 4px 12px rgba(255, 65, 108, 0.3);
    }

    /* Results Section */
    .stMarkdown {
        background: rgba(255, 255, 255, 0.1);
        color: #000 !important;
        padding: 15px;
        border-radius: 10px;
        font-size: 3rem;
        text-align: center;
        font-family: 'Raleway', sans-serif;
        box-shadow: 0 4px 10px rgba(255, 255, 255, 0.2);
    }
    .result-text {
        background: rgba(255, 255, 255, 0.1);
        padding: 15px;
    }

    /* Success & Warning Messages */
    .stSuccess {
        background: rgba(0, 255, 0, 0.2) !important;
        color: #00ff00 !important;
        border: 2px solid #00ff00;
        border-radius: 10px;
        padding: 10px;
        font-size: 20px;
        font-family: 'Raleway', sans-serif;
    }

    .stWarning {
        background: rgba(255, 204, 0, 0.2) !important;
        color: #ffcc00 !important;
        border: 2px solid #ffcc00;
        border-radius: 10px;
        padding: 10px;
        font-family: 'Raleway', sans-serif;
    }

    /* Tab Styling */
    .stTabs>div>button {
        background: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: none;
        border-radius: 10px;
        padding: 12px 20px;
        font-size: 1.1rem;
        font-weight: bold;
        font-family: 'Orbitron', sans-serif;
        transition: all 0.3s ease;
    }

    .stTabs>div>button:hover {
        background: rgba(255, 255, 255, 0.2) !important;
        color: #00c6ff !important;
    }

    .stTabs>div>button:focus {
        background: rgba(255, 255, 255, 0.2) !important;
        color: #00c6ff !important;
    }

    </style>
""", unsafe_allow_html=True)

# Streamlit UI
st.markdown("<h1 class='main-title'>🔄 Unit Converter</h1>", unsafe_allow_html=True)

unit_types = list(types.keys())
selected_type = st.sidebar.selectbox("Select Unit Type:", unit_types)

# Help & About Section
st.sidebar.markdown("""
    ## ℹ️ Help & About
    - Select a unit type from the dropdown.
    - Choose the units you want to convert between.
    - Enter a value and click **Convert**.
    - The result will be displayed and read aloud.
""")

unit_options = list(types[selected_type].keys())
from_unit = st.selectbox("From Unit:", unit_options)
to_unit = st.selectbox("To Unit:", unit_options)
value = st.number_input("Enter Value:", min_value=0.00, format="%.4f")

# Conversion Function
def convert(value, from_unit, to_unit, unit_type):
    try:
        if unit_type == "Temperature":
            temp = value if from_unit == "celsius" else (value - 32) * 5/9 if from_unit == "fahrenheit" else value - 273.15
            return types[unit_type][to_unit](temp)
        else:
            return value * (types[unit_type][to_unit] / types[unit_type][from_unit])
    except KeyError:
        st.error("Invalid unit type or unit selected.")
        return None

# Speech Function
def speak(text):
    try:
        text = text.replace(" 0 ", " zero ")  
        text = text.replace("0.", "zero point ")  

        tts = gTTS(text=text, lang="en")
        file_path = "output.mp3"
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.mixer.init()

        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except PermissionError:
                time.sleep(1)
                os.remove(file_path)

        tts.save(file_path)
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.mixer.init()

        time.sleep(0.5)

        try:
            os.remove(file_path)
        except PermissionError:
            time.sleep(1)
            os.remove(file_path)
    except Exception as e:
        st.error(f"Error in speech synthesis: {e}")

if st.button("Convert"):
    result = convert(value, from_unit, to_unit, selected_type)
    if result is not None:
        result_text = f"{value} {from_unit} = {result:.4f} {to_unit}"
        st.markdown(f"<h3 class='stMarkdown'>{result_text}</h3>", unsafe_allow_html=True)
        speak(result_text)
