!pip install SpeechRecognition pydub openai-whisper torch

import speech_recognition as sr
import whisper
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

def record_and_transcribe():
    # Initialize recognizer and model
    recognizer = sr.Recognizer()
    model = whisper.load_model("base")
    
    print("Starting recording... Speak now!")
    print("(Press Ctrl+C to stop recording)")
    
    try:
        with sr.Microphone() as source:
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=1)
            
            # Record audio
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            
            # Save to temporary file
            with open("temp_audio.wav", "wb") as f:
                f.write(audio.get_wav_data())
            
            print("\nProcessing with Whisper...")
            
            # Transcribe
            result = model.transcribe("temp_audio.wav")
            
            # Print clean output
            print("\n" + "="*40)
            print("TRANSCRIPTION RESULT:")
            print("="*40)
            print(result["text"])
            print("="*40)
            
    except KeyboardInterrupt:
        print("\nRecording stopped by user")
    except Exception as e:
        print(f"\nError occurred: {e}")

# Run the function
record_and_transcribe()
