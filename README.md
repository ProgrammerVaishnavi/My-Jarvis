# My-Jarvis
# Jarvis AI Assistant 🤖

A simple **voice-controlled virtual assistant** built in Python. Jarvis can perform tasks such as searching Wikipedia, opening websites, playing music, telling the time, and sending emails.  

---

## Features

- Greet the user based on the time of day  
- Search Wikipedia and read summaries aloud  
- Open YouTube, Google, and Brave browser  
- Play music from a specified directory  
- Tell the current system time  
- Send emails securely using environment variables  

---

## Prerequisites

- Python 3.x  
- Windows OS (for SAPI5 voice engine; can be adapted for Linux/Mac with `espeak`)  

### Required Python Libraries
Install the dependencies using `pip`:

```bash
pip install pyttsx3 speechrecognition wikipedia
