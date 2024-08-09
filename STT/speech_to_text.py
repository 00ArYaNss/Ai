import speech_recognition as sr

recognizer = sr.Recognizer()

print("I am listening...")

with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(source)
        
        print("Listening for 2 seconds...")

        audio = recognizer.listen(source, timeout=2)
    
        query = recognizer.recognize_google(audio, language='en')
        print(query)


