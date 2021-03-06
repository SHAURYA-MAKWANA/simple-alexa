import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia 
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)

    except:
       pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'I love you' in command:
        talk('Sorry I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'search' in command:
        wik = command.replace('search', '')
        result = wikipedia.search(wik)
        talk('here is what i found ', (result))
    elif 'shaurya' or 'shaurya makwana' in command:
        talk("he is my owner shaurya makwana")
    elif 'ok google' or 'hey google' in command:
        talk("have a test of your senses they aren't awareful")
    else:
        talk('Please say the command again.')    
        
   


while True:
    run_alexa()