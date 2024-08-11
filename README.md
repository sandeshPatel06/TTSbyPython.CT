# Flask Text-to-Speech Application

## Overview

This Flask web application provides a simple interface to convert text into speech using the `pyttsx3` library. Users can input text, select a language, choose a voice, and adjust the speech rate and volume. The application then generates an MP3 file with the spoken text and allows users to download it.

## Features

- **Multiple Languages**: Supports various languages for text-to-speech conversion.
- **Voice Selection**: Allows users to choose from available voices.
- **Customizable Speech Properties**: Adjust speech rate and volume.
- **MP3 Output**: Generates and downloads an MP3 file with the spoken text.

## Technologies

- **Flask**: Web framework for Python.
- **pyttsx3**: Python library for text-to-speech conversion.

## Installation

1. **Clone the Repository**:

    ```bash
    git clone  https://github.com/sandeshPatel06/TTSbyPython.git
    cd your-repository
    ```

2. **Create and Activate a Virtual Environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**:

    ```bash
    python app.py
    ```

    The application will be available at `http://127.0.0.1:5000/`.

## API Endpoints

- **`GET /`**: Render the main interface with language options.
- **`GET /voices`**: Retrieve available voice options.
- **`POST /convert`**: Convert text to speech and return an MP3 file.

## Usage

1. Open the application in your browser.
2. Input the text you want to convert to speech.
3. Select the language and voice.
4. Adjust the speech rate and volume.
5. Click "Convert" to generate and download the MP3 file.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, you can reach me at [sandeshpatel.sp.93@gmail.com](mailto:sandeshpatel.sp.93@gmail.com).

## GitHub

[GitHub Repository](https://github.com/sandeshPatel06/TTSbyPython.CT.git)
![image](https://github.com/user-attachments/assets/bb646975-55be-443f-aec3-9f1c9a7b98e1)

