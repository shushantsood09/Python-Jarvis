# The very first step is to convert the voice to text.
# So, for that we will require a speech recogniser.
import pyttsx3  # text-to-speech conversion library in Python
import speech_recognition as sr  # Module for speech recognition
import webbrowser  # Module for web search.
import datetime  # Module for Date and Time
import pyjokes  # Module for jokes.
import smtpd  # Module for sending mails.
import os  # Module for interacting with Operating System.
import time 

def speechToText():
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak...")
        recognize.adjust_for_ambient_noise(source)
        audio = recognize.listen(source)
        try:
            print("Recognizing.....")
            recievedData = recognize.recognize_google(audio)
            print(recievedData)
            return recievedData
        except sr.UnknownValueError:
            print("Not Understanding")


def textToSpeech(data):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Here 0 for male voice and 1 for female voice.
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 130)
    engine.say(data)
    engine.runAndWait()


if __name__ == '__main__':

    if "poppy" in speechToText().lower():
    # print("test")
        while True:
            dataInfo = speechToText().lower()
            if "your name" in dataInfo:
                name = "my name is poppy"
                textToSpeech(name)
            elif "old are you" in dataInfo:
                age = "I am 1 years old"
                textToSpeech(age)

            elif "time" in dataInfo:
                time = datetime.datetime.now().strftime("%I%M%p")
                textToSpeech(time)

            elif "youtube" in dataInfo:
                webbrowser.open("https://www.youtube.com/")

            elif "google" in dataInfo:
                webbrowser.open("https://www.google.com/")

            elif "facebook" in dataInfo:
                webbrowser.open("https://www.facebook.com/")

            elif "instagram" in dataInfo:
                webbrowser.open("https://www.instagram.com/")

            elif "linkedin" in dataInfo:
                webbrowser.open("https://www.linkedin.com/")

            elif "joke" in dataInfo:
                joke = pyjokes.get_joke(language="en", category="neutral")
                print(joke)
                textToSpeech(joke)

            elif "song" in dataInfo:
                address = 'D:\Music'
                listsong = os.listdir(address)
                print(listsong)
                os.startfile(os.path.join(address, listsong[0]))

            elif "exit" in dataInfo:
                textToSpeech("Thank you for using me!")
                break

            time.sleep(5)

    else:
        print("Thank You!!")

# textToSpeech("Hello, welcome to python program")
