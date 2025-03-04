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
    pip install streamlit==1.22.0
    pip install pygame==2.1.2
    pip install gtts==2.3.2
    pip install speechrecognition==3.8.1
    ```

4. If you encounter issues with `pygame`, ensure you have the necessary build tools installed. On Windows, you can install the Visual Studio Build Tools from [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

5. To further troubleshoot the installation issues, you can try installing the dependencies one by one to identify which package is causing the problem. Additionally, ensure that you have the necessary build tools installed on your system.

6. Run the Streamlit application:
    ```sh
    streamlit run unit-convertor.py
    ```

## Dependencies

- Streamlit
- Pygame
- gTTS
- SpeechRecognition

Make sure to install the dependencies using the provided `requirements.txt` file.
