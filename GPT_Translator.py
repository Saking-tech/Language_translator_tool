import speech_recognition as sr
import pyttsx3
import openai

apikey = "API_KEY"
openai.organization = "org-49qwvNPbihsNA0wsH4N1acHi"
openai.api_key = apikey
model_engine = "gpt-4o-mini-2024-07-18"

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
    my_lang = "hi-IN"
elif my_lang == "French":
    my_lang = "fr-FR"
text = listen_speech("Taking your input",my_lang)


if lang == "Hindi":
    engine.setProperty('voice', voices[3].id)
elif lang == "French":
    engine.setProperty('voice', voices[5].id)
    
prompt = f"Convert the \" {text} \" into {lang}"
response = openai.ChatCompletion.create(
    model="gpt-4o-mini-2024-07-18",
    messages=[{
        "role":"user",
        "content": prompt}]
)
saves = response.choices[0].message.content
print(saves)
speak_text(saves)




