import os
import streamlit as st
from gtts import gTTS

# Streamlit UI
st.markdown("<h1 class='main-title'>🔄 Unit Converter</h1>", unsafe_allow_html=True)

st.sidebar.title("Conversion Types")

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
    },
     "Speed": {"meter per second": 1, "kilometer per hour": 3.6, "mile per hour": 2.23694},
    "Area": {
        "square meter": 1, "square kilometer": 1e-6, "square centimeter": 1e4, "square millimeter": 1e6,
        "hectare": 1e-4, "acre": 0.000247105, "square mile": 3.861e-7

},
}

# Expanded with additional categories: Energy, Speed, Area, Pressure, Data Storage
types = {
    "Length": {"meter": 1, "kilometer": 0.001, "centimeter": 100, "millimeter": 1000, "mile": 0.000621371,
                "yard": 1.09361, "foot": 3.28084, "inch": 39.3701, "nautical mile": 0.000539957},
    "Weight": {"kilogram": 1, "gram": 1000, "pound": 2.20462, "ounce": 35.274, "ton": 0.001},
    "Temperature": {"celsius": lambda c: c, "fahrenheit": lambda c: (c * 9/5) + 32, "kelvin": lambda c: c + 273.15},
    "Time": {"second": 1, "minute": 1/60, "hour": 1/3600, "day": 1/86400},
    "Volume": {"liter": 1, "milliliter": 1000, "gallon": 0.264172},
    "Energy": {"joule": 1, "kilojoule": 0.001, "calorie": 0.239006},
    "Speed": {"meter per second": 1, "kilometer per hour": 3.6, "mile per hour": 2.23694},
    "Area": {"square meter": 1, "square kilometer": 0.000001, "acre": 0.000247105},
    "Pressure": {"pascal": 1, "bar": 0.00001, "atmosphere": 0.00000986923},
    "Data Storage": {"bit": 1, "byte": 8, "kilobyte": 8192, "megabyte": 8.389e+6}
}



# Collapsible About Section
with st.expander("ℹ️ About Unit Converter"):
    st.markdown("""
    This app allows you to convert between various units of measurement. 

    ### How to Use:
    1. Select a **unit type** (e.g., Length, Weight, Temperature).
    2. Choose **From Unit** and **To Unit**.
    3. Enter a **value** and click **Convert**.
    4. The result will be displayed and spoken aloud.

    ### Features:
    ✅ Supports multiple unit types
    ✅ Real-time voice output
    ✅ Sleek and modern UI
    ✅ Works on all devices
    """)
conversion_type = st.sidebar.radio("", list(types.keys()))

# User Input
unit_options = list(types[conversion_type].keys())
from_unit = st.selectbox("From Unit", unit_options)
to_unit = st.selectbox("To Unit", unit_options)
value = st.number_input("Enter Value")

# Conversion Function
def convert(value, from_unit, to_unit, unit_type):
    if unit_type == "Temperature":
        temp = value if from_unit == "celsius" else (value - 32) * 5/9 if from_unit == "fahrenheit" else value - 273.15
        return types[unit_type][to_unit](temp)
    else:
        return value * (types[unit_type][to_unit] / types[unit_type][from_unit])

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Raleway:wght@500;700&family=Orbitron:wght@500&display=swap');

    /* Global styles */
   .custom-about {
       
    }

    /* Main App Container */
    .stApp {
        background-color: #8CC48F; /* Dark blue background */
        color: #ffffff; /* White text */
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
    }

   /* Sidebar Styling */
.stSidebar {
    background: linear-gradient(190deg, #558D59, #16213e) !important;
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

    
# Speech Function
def speak(text):
    text = text.replace(" 0 ", " zero ")  
    text = text.replace("0.", "zero point ")  

    file_path = "output.mp3"
    tts = gTTS(text=text, lang="en")
    tts.save(file_path)

    return file_path  # Return MP3 file path instead of playing sound
#About Section


if st.button("Convert"):
    result = convert(value, from_unit, to_unit, selected_type)
    result_text = f"{value} {from_unit} = {result:.4f} {to_unit}"
    
    st.markdown(f"<h3 class='result-text'>{result_text}</h3>", unsafe_allow_html=True)

    # Get the MP3 file path
    audio_file = speak(result_text)

    # Play the audio in Streamlit
    with open(audio_file, "rb") as f:
        st.audio(f.read(), format="audio/mp3")
    
    # Delete the file to clean up
    os.remove(audio_file)

    


