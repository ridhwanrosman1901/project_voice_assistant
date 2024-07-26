# Voice Assistant Project

This project is a simple voice assistant built using Python. The assistant can greet the user based on the time of day and recognize voice commands using Google's speech recognition service.

## Features

- Text-to-speech greeting based on the time of day.
- Voice recognition to take commands from the user.

## Requirements

- Python 3.12+
- `pyttsx3` library for text-to-speech.
- `speech_recognition` library for speech-to-text.
- `pyaudio` library for accessing the microphone.

## Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/ridhwanrosman1901/voice_assistant.git
   cd voice_assistant

2. **Create a Virtual Environment (optional but recommended)**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Required Libraries**

   ```sh
   pip install pyttsx3 speechrecognition pyaudio setuptools

## Usage

1. **Run the Voice Assistant**

   ```sh
   python voice_assistant.py

2. **Interact with the Assistant**

    The assistant will greet you and prompt you to give a voice command.

## Troubleshooting

- **ModuleNotFoundError: No module named 'distutils'**
  If you encounter this error, install the setuptools package:

   ```sh
   pip install setuptools

- **PyAudio Installation Issues**
  f you have trouble installing pyaudio, you can download the appropriate wheel file from PyAudio's unofficial binaries and install it using pip.

   ```sh
   pip install path/to/downloaded/pyaudio.whl

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests with your improvements.

## License

This project is licensed under the MIT License. See the **'LICENSE'** file for more details.

## Contact

For any inquiries or feedback, please reach out to me.
