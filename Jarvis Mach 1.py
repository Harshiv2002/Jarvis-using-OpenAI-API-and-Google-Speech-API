# ** Jarvis Working Mach 1 **
import speech_recognition as sr
import pyttsx3  
import openai

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    # create a speech recognition object
    r = sr.Recognizer()
    # use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        # listen for user speech
        audio = r.listen(source)
    # convert the speech to text using Google's speech recognition API
    try:
        text = r.recognize_google(audio)
        print("You: " + text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

while True:
    # listen for user speech
    text = listen().lower()
    #text = "hello"
    if "hello" in text:
        speak("Hello! How can I assist you?")
    elif "how are you" in text:
        speak("I'm fine, thank you. How about you?")
    elif "what's your name" in text:
        speak("My name is Jarvis. How may I help you?")
    elif "bye" in text:
        speak("Goodbye!")
        break
    else:
        try:
            openai.api_key = "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"
            messages = [
            {"role":"system","content":"you are a helpful assistant"}
            #{"role":"system","content":"you are a recruiter who asks interview questions."}
            ] 

            completion = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = [
                    {"role":"user","content":text}
                ]
            )

            text = text.replace("jarvis", "OpenAI")
            content = text  
            chat_response = completion.choices[0].message.content
            chat_response = chat_response.replace("OpenAI","Jarvis").replace("created by Jarvis","created by Harshiv")  

            print(f'Jarvis:{chat_response}')
            speak(chat_response)
            messages.append({"role":"assistant","content":chat_response})
        except:
            print("Sorry, something went wrong!")
            speak("Sorry, something went wrong!")