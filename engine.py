import pyttsx3
import speech_recognition as sr
import pywhatkit
import googletrans
import pyautogui
import tkinter as tk
from threading import Thread
import datetime
import os
import subprocess


# Initialize the text-to-speech engine
engine = pyttsx3.init()
recognizer = sr.Recognizer()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def record_audio():
   
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio

def process_command():
    audio = record_audio() 
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        if "hello" in command:
            speak("Hello! How can I assist you?")
        elif "how are you" in command:
            speak("I'm doing well, thank you for asking!")
        elif "open file" in command:
            open_file(command)
        elif "save file" in command:
            save_file(command)
        elif "access internet" in command:
            access_internet()
        elif "search for" in command:
            search_term = command.split("search for ")[-1]
            speak("Searching for " + search_term)
            pywhatkit.search(search_term)
        elif "translate" in command:
            translate_text(command)
        elif "reply to message" in command:
            reply_to_message()
        elif "weather report" in command:
            get_weather_report()
        elif "offline google" in command:
            offline_google_search()
        elif "online google" in command:
            online_google_search()
        elif "take screenshot" in command:
            take_screenshot()
        elif "scan text" in command:
            scan_text()
        elif "current time" in command:
            get_current_time()
        elif "play song" in command:
            play_song(command)
        elif "open game" in command:
            open_game(command)
        else:
            speak("I'm sorry, I didn't understand that command.")
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        speak("Sorry, there was an error with the speech recognition service.")

def open_file(command):
    # Extract filename from command and open the file
    file_name = command.split("open file ")[-1]
    try:
        os.startfile(file_name)
    except FileNotFoundError:
        speak("Sorry, the file " + file_name + " was not found.")

def save_file(command):
    # Extract filename and content from command and save to file
    try:
        file_name = command.split("as ")[-1].split(" save file")[0]
        content = command.split("as ")[0].split("save file ")[-1]
        with open(file_name, 'w') as file:
            file.write(content)
        speak("File " + file_name + " saved successfully.")
    except Exception as e:
        speak("Sorry, there was an error saving the file.")

def access_internet():
    speak("Internet access is not available in offline mode.")

def translate_text(command):
    translator = googletrans.Translator()
    try:
        text_to_translate = command.split("translate ")[-1]
        translated_text = translator.translate(text_to_translate, dest='en').text
        speak("The translated text is: " + translated_text)
    except Exception as e:
        speak("Sorry, there was an error translating the text.")

def reply_to_message():
    speak("Messaging service is not available in offline mode.")

def get_weather_report():
    speak("Weather report service is not available in offline mode.")

def offline_google_search():
    speak("Offline Google search service is not available.")

def online_google_search():
    speak("Please tell me what you want to search for.")
    search_term = record_audio()
    try:
        pywhatkit.search(search_term)
    except Exception as e:
        speak("Sorry, there was an error performing the online Google search.")

def take_screenshot():
    # Take a screenshot and save it
    image = pyautogui.screenshot()
    image.save("screenshot.png")
    speak("Screenshot taken and saved successfully.")

def scan_text():
    speak("Text scanning service is not available in offline mode.")

def get_current_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak("The current time is " + current_time)

def play_song(command):
    # Extract song name from command and play it
    song_name = command.split("play song ")[-1]
    pywhatkit.playonyt(song_name)

def open_game(command):
    # Extract game name from command and open it
    game_name = command.split("open game ")[-1]
    try:
        subprocess.Popen(game_name)
    except FileNotFoundError:
        speak("Sorry, the game " + game_name + " was not found.")

def start_voice_search():
    Thread(target=process_command).start()

# Create the GUI
root = tk.Tk()
root.title("Jarvis")

# Add a button for voice search
voice_search_button = tk.Button(root, text="Voice Search", command=start_voice_search)
voice_search_button.pack()

root.mainloop()
