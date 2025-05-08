
# Real-Time Speech-to-Text Transcription using Whisper

## Project Overview
This project is a real-time speech recognition system that records audio from a microphone and transcribes it into text using OpenAI's Whisper model. It's a simple demonstration of using AI-based tools for converting spoken words into readable text.

## Technologies Used
- **Python 3**: Programming language
- **SpeechRecognition**: Library for audio input via microphone
- **openai-whisper**: Whisper model for transcription
- **torch**: Backend for running Whisper model
- **pydub**: (Optional) For further audio processing
- **Google Colab / Jupyter Notebook**: For running the code

## Usage
1. Clone or download this repository.
2. Install the required libraries using the following command:

```bash
pip install SpeechRecognition pydub openai-whisper torch
```

3. Run the `main.py` file to start recording and transcribing speech.

## Output
After successful execution, the program records audio through the microphone and prints the transcribed text on the console. You can find a screenshot of the output in the `output.png` file.

## Conclusion
The project successfully captures audio from the user and transcribes it accurately using the Whisper base model. It demonstrates real-time audio processing and serves as a foundation for more complex voice assistant systems.
