# Jarvis AI Assistant
# Author: Your Name
# Description:
#   A simple voice-controlled virtual assistant that can perform tasks like:
#   - Searching Wikipedia
#   - Opening websites (YouTube, Google, Brave browser)
#   - Playing music
#   - Telling the current time
#   - Sending emails (requires environment variables for credentials)

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# ================== Text-to-Speech Engine Setup ==================
engine = pyttsx3.init('sapi5')  # SAPI5 is for Windows voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice (voices[0] = male)
engine.setProperty('rate', 170)  # Speaking speed


def speak(audio):
    """Speak out the given text using text-to-speech engine."""
    engine.say(audio)
    engine.runAndWait()


# ================== Wish User ==================
def wishMe():
    """Wish the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis, Sir. Please tell me how may I help you.")


# ================== Take Voice Command ==================
def takecommand():
    """
    Listen to microphone input and return recognized text.
    Returns "None" if recognition fails.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1  # Seconds of silence before stop listening
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')  # Using Google Speech API
        print(f"User said: {query}\n")
    except Exception:
        print("Say that again please....")
        return "None"
    return query


# ================== Send Email ==================
def sendEmail(to, content):
    """Send an email using Gmail SMTP server."""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Credentials must be set as environment variables for security
    email = os.getenv("JARVIS_EMAIL")
    password = os.getenv("JARVIS_PASSWORD")

    if not email or not password:
        raise ValueError("Email credentials not found. "
                         "Please set JARVIS_EMAIL and JARVIS_PASSWORD as environment variables.")

    server.login(email, password)
    server.sendmail(email, to, content)
    server.close()


# ================== Main Program ==================
if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        # Search Wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except Exception:
                speak("Sorry, I could not find any results on Wikipedia.")

        # Open YouTube
        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube")

        # Open Google
        elif 'open google' in query:
            webbrowser.open("https://google.com")
            speak("Opening Google")

        # Play Music
        elif 'play music' in query:
            speak("Ok, playing music for you")
            music_dir = r'C:\Users\krishna\OneDrive\Music\Playlists'  # Change this path if needed
            if os.path.exists(music_dir):
                os.startfile(music_dir)
            else:
                speak("Music folder not found.")

        # Tell Time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        # Open Brave Browser
        elif 'open brave' in query:
            speak("Ok, opening Brave")
            brave_path = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
            if os.path.exists(brave_path):
                os.startfile(brave_path)
            else:
                speak("Sorry, I couldn't find Brave on your system.")

        # Send Email
        elif 'email to vaishnavi' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = os.getenv("JARVIS_RECIPIENT_EMAIL", "example@example.com")
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, my friend. I am not able to send this email.")
