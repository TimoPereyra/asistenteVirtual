import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

name = 'kakaroto'
def talk(text):
    engine.say(text)
    engine.runAndWait()

def escuchar():
    try:
        with sr.Microphone()as source:
            print("escuchando.....")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice,language="es")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name,'')
                print(rec)
            else:
                rec = -1
    except:
        pass
    return rec    

def correr():
    rec = escuchar()
    if (rec == -1):
        talk("Error en el nombre pa ")
    elif 'reproduce' in rec:
        music = rec.replace('reproduce','')

        talk('Reproduciendo'+music)
        pywhatkit.playonyt(music)

    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las "+hora)

    elif 'busca' in rec:
        order = rec.replace('busca','')
        info = wikipedia.summary(order, 1)
        talk(info)
    else:
        talk("En algo le erraste mi rey")

while True:        
    correr()