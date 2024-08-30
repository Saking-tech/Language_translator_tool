import speech_recognition as sr
import pyttsx3
import openai
from googletrans import Translator

# Initialize the recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def listen_speech(text,lang):
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print(text)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio,language=lang)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

def speak_text(text):
    engine.say(text)
    engine.runAndWait()  # Blocks while processing all the currently queued commands

def chatbot_response(text):
    
    return f"You said: {text}"

# Main loop
speak_text("In which Language you will talk here?")
my_lang = listen_speech("Your Language","en-US")
speak_text("Which Language you want to Listen?")
lang = listen_speech("Converting Language","en-US")
speak_text("Now go on with your words")

if my_lang == "Hindi":
    my_lang = "hi"
elif my_lang == "French":
    my_lang = "fr"
else:
    my_lang = "en"
text = listen_speech("Taking your input",my_lang)


if lang == "Hindi":
    lang = "hi"
    engine.setProperty('voice', voices[3].id)
elif lang == "French":
    lang = "fr"
    engine.setProperty('voice', voices[5].id)
else:
    lang = "en"

translator = Translator()
translated = translator.translate(text, src=my_lang, dest=lang).text
print(translated)
speak_text(translated)




