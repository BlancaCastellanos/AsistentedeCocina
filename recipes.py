import speech_recognition as sr 
import time 
from time import ctime 
import webbrowser
import playsound
import os
import random
from gtts import gTTS


r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexa_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try: 
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            alexa_speak('I am sorry, i did not understand you')
        except sr.RequestError:
            alexa_speak('I am sorry, conection error')
        return voice_data


def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang="es")
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)



def respond(voice_data):
    if 'what is your name' in voice_data:
        alexa_speak('My name is Jimena')
    if 'what time is it'in voice_data:
        alexa_speak(ctime())
    if 'search' in voice_data:
        buscar = record_audio('What ingredient do you want to look for?')
        url = 'https://google.com/search?q=' + buscar
        webbrowser.get().open(url)
        alexa_speak('This is what i found for: ' + buscar)

    if "equivalence" in voice_data:
        buscar = record_audio("What equivalence of measure do you want to find?")
        url = 'https://google.com/search?q=' + buscar
        webbrowser.get().open(url)
        alexa_speak('This is what i found for: ' + buscar)

    if 'quesadilla recipe' in voice_data:
        alexa_speak('The ingredients are harina or maiz tortillas, cheese of your choice, vegetables and sauce to taste. Do you want to hear more details about the recipe?')
    if 'quesadilla details' in voice_data:
        alexa_speak('The way of preparation is to put our tortillas over a low heat, once hot, place the cheese on them, fold them in half, and wait until the cheese is gratin, finally we serve and enjoy.')
    if 'sandwich recipe' in voice_data:
        alexa_speak('The ingredients are 2 portions of bread, ham, cheese of your choice, tomato, lettuce, mayonnaise, mustard and butter to taste. Do you want to hear more details about the recipe?')
    if 'sandwich details' in voice_data:
        alexa_speak('The way of preparation is to brown our bread with butter, place the mayonnaise and mustard to taste to our breads, then add the ham, cheese, vegetables, finally we serve and enjoy.')
    if 'healthy smoothie' in voice_data:
        alexa_speak('The ingredients are half a mango, half a banana, 1 ounce of oats, 15 grams of peanut butter, 500 ml of milk of your choice.Do you want to hear more details about the recipe?')
    if 'smoothie details' in voice_data:
        alexa_speak('The way of preparation is to add the mango, banana, oatmeal, peanut butter, milk, blend, serve and enjoy.')
    if 'bye' in voice_data:
        exit()

time.sleep(1)
alexa_speak('How can i help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)