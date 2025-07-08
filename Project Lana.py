import speech_recognition as sr
import webbrowser
import pyttsx3
import playmusic

recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def processcommand(c):
    if"open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif"open google" in c.lower():
        webbrowser.open("https://google.com")
    elif"open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif"open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link= playmusic.music[song]
        webbrowser.open(link)




if __name__ == "__main__":
    speak("Initializing Lana....")
    while True:
     
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=8, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if(word.lower() == "lana"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Lana Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)


        except Exception as e:
            print("Error; {0}".format(e))

