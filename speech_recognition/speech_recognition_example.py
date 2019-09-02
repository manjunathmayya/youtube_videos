import speech_recognition as sr
import os

# obtain audio from the microphone
r = sr.Recognizer()

while True:

    with sr.Microphone() as source:         
        
        audio = r.listen(source, phrase_time_limit = 5)    
        
    try:

        text = r.recognize_google(audio).lower()
        
        if 'open' in text:
            if 'notepad' in text:
                os.system("start notepad.exe")
           
            if 'chrome' in text:
                os.system("start chrome.exe") 
            
                
    except Exception:
        print("Something went wrong in Google Speech Recognition")
