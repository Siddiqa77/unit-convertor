# Unit Converter

This is a Streamlit-based unit converter application that supports various unit types including length, weight, temperature, time, and volume.

## Setup Instructions

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd unit-convertor
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. If you encounter issues with `pygame`, install it separately:
    ```sh
    pip install pygame
    ```

5. Run the Streamlit application:
    ```sh
    streamlit run unit-convertor.py
    ```

## Dependencies

- Streamlit
- Pygame
- gTTS
- SpeechRecognition

Make sure to install the dependencies using the provided `requirements.txt` file.
