import wolframalpha
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
import datetime
import tkinter
from tkinter import *
import shutil


voiceEngine = pyttsx3.init('sapi5')
voices = voiceEngine.getProperty('voices')
voiceEngine.setProperty('voice', voices[1].id)


def speak(text):
    voiceEngine.say(text)
    voiceEngine.runAndWait()


def greeting():
    print('greeting')
    time = int(datetime.datetime.now().hour)
    global uname, asname
    if 0 <= time < 12:
        speak('Good Morning!')

    elif time < 18:
        speak('Good Afternoon!')

    else:
        speak('Good Evening!')

    asname = 'Pygen'
    speak('I am your Voice Assistant,')
    speak(asname)
    print('I am your Voice Assistant,', asname)


def getName():
    global uname
    speak('What is your name?')
    uname = takeCommand()
    print('Name: ', uname)
    columns = shutil.get_terminal_size().columns
    speak('How can I help you, ')
    speak(uname)


def takeCommand():
    global showCommand
    showCommand.set('Listening...')
    cmdLabel.config()

    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening to the user')
        recog.pause_threshold = 1
        userInput = recog.listen(source)

    try:
        print('Recognizing command')
        command = recog.recognize_google_cloud(userInput, language='en-in')
        print(f'Command is: {command}\n')

    except Exception as e:
        print(e)
        print('Unable to recognize voice')
        return 'None'

    return command


def callAssistant():

    uname = ''
    asname = ''
    os.system('cls')
    greeting()
    getName()
    print(uname)

    while True:

        command = takeCommand().lower()
        print(command)

        if 'hello' or 'good morning' or 'good afternoon' or 'good evening'\
           in command:
            speak(f'{command} to you too, hope you are well!')

        elif 'how are you' in command:
            speak('I am fine, thank you. How are you?')

        elif 'who are you' or 'your name' in command:
            speak(f'I am {asname}, your virtual assistant!')

        elif 'time' in command:
            strTime = datetime.datetime.now()
            curTime = str(strTime.hour) + 'hours' + str(strTime.minute)\
                + 'minutes' + str(strTime.second) + 'seconds'
            speak(f'The time is {curTime}')
            print(curTime)

        elif 'wikipedia' in command:
            speak('Searching Wikipedia')
            command = command.replace('wikipedia', '')
            results = wikipedia.summary(command, sentences=3)
            speak('This is what I found')
            speak(results)
            print(results)

        elif 'open youtube' in command:
            speak('Opening Youtube')
            webbrowser.open('youtube.com')

        elif 'open google' in command:
            speak('Opening Google')
            webbrowser.open('google.com')

        elif 'joke' in command:
            speak(pyjokes.get_joke())

        elif 'exit' or 'close' in command:
            speak('Ok, Goodbye!')
            exit()

        elif 'i love you' in command:
            speak('I love you too!')

        elif 'what is' or 'who is' in command:

            client = wolframalpha.Client('API_ID')
            res = client.query(command)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)

            except StopIteration:
                print('no results')
                speak('no results')

        elif 'search' in command:
            command = command.replace('search', '')
            webbrowser.open(command)


wn = tkinter.Tk()
wn.title('Pygen Voice Assistant')
wn.geometry('700x300')
wn.config(bg='Lightblue1')

Label(wn, text='Meet Pygen, your new voice assistant', bg='LightBlue1',
      fg='black', font=('Georgia', 15)).place(x=50, y=10)

Button(wn, text='Start', bg='gray', font=('Georgia', 15),
       command=callAssistant).place(x=290, y=100)

showCommand = StringVar()
cmdLabel = Label(wn, textvariable=showCommand, bg='LightBlue1',
                 fg='black', font=('Georgia', 15))
cmdLabel.place(x=250, y=150)

wn.mainloop()
