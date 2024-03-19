import pyttsx3 
import speech_recognition as sr
import datetime 
import wikipedia 
import webbrowser
# pyttsx3.speak('kshitij Raj shukla')
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <12:
        speak('good morning my sir')
    
    elif hour >= 12 and hour<18:
        speak('good afternoon my sir')
    
    else:
        speak('good evening my sir')
    
    speak('how can i help you sir')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('computing...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('recognizing...')
        query = r.recognize_google(audio, language = 'en-in')
        print(f'user said: \n{query}')
    
    except Exception as e:
        print('say that again sir...')
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('searching in wikipedia...')
            query = query.replace('wikipedia'," ") 
            results = wikipedia.summary(query, sentences = 4)
            speak('according to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('searching for youtube...')
            webbrowser.open('http://www.youtube.com/watch')

        elif 'open google' in query:
            speak('searching for google...')
            webbrowser.open('http://www.google.com')
        elif 'open github' in query:
            speak('searching for github...')
            webbrowser.open('https://github.com/')

        else:
            speak('these are the end of my capabilities, sir...')

