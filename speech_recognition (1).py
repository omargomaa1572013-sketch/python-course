import SpeechRecoginition  as sr
import sys
import pyttsx3
engine = pyttsx3.init()
rec = sr.Recognizer()
with sr.Microphone() as src:
    while True:
        print("say something ...")
        
        audio = rec.listen(src)
        text = rec.recognize_google(audio)
        if text in "hello":
            print(text)
            engine.say("hi how are you")
            engine.runAndWait()
        elif text in ["fine","good","great"]:
            print(text)
            engine.say("nice")
            engine.runAndWait()
        elif text in "close":
            print(text)
            engine.say("godbye")
            engine.runAndWait()
            sys.exit()
        else:
            print((text))
            engine.say("I don't understand")
            engine.runAndWait()
        
            