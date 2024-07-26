import pyttsx3
import datetime
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 --> Male voice

def speak(text):
    
    # Convert text to speech.
    
    engine.say(text)
    engine.runAndWait()

def wishMe():
    
    # Wishes the user based on the time of day.
    
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')

def takeCommand():
    
    # Listens to the user's input from the microphone and returns it as a string.
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Listening...')
        r.pause_threshold = 1
        user_audio = r.listen(source)
    try:
        print('Recognizing User Input...')
        query = r.recognize_google(user_audio, language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        print('Say that again, please...')
        return "None"
    return query

# Main function
if __name__ == "__main__":
    wishMe()
    speak('Hello sir, I am David, your personal voice assistant. Please tell me, how can I help you?')
    takeCommand()
