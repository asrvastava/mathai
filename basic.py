from logging import exception
import pyttsx3
import speech_recognition as sr

abc=pyttsx3.init()

def speak(audio):
    abc.say(audio)
    abc.runAndWait()

try:
    def takecommand():
        r=sr.Recognizer()

        with sr.Microphone() as source:
            r.pause.threshold=3
            audio=r.listen(source)

            try:
                print("recognizing")
                try:
                    query=r.recognize_google(audio)
                except Exception:
                    speak("could you say it again")

                print(query)
                return query
            except Exception as e:
                print(e)    
except Exception as k:
    print(k)