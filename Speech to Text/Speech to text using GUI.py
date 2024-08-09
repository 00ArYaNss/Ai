import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import threading

# Initialize the recognizer
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Variables to manage recording state
recording = False
audio_data = None

def start_recording():
    global recording, audio_data
    if recording:
        messagebox.showinfo("Info", "Recording is already in progress.")
        return
    
    recording = True
    audio_data = None
    status_label.config(text="Recording...")
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    
    def record_audio():
        global audio_data
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio_data = recognizer.listen(source)
    
    # Run the recording in a separate thread
    threading.Thread(target=record_audio).start()

def stop_recording():
    global recording, audio_data
    if not recording:
        messagebox.showinfo("Info", "No recording in progress.")
        return
    
    recording = False
    status_label.config(text="Recording stopped.")
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

        # Transcribe the audio
    query = recognizer.recognize_google(audio_data, language='en')
    result_label.config(text="Transcription: " + query)
    




app = tk.Tk()
app.geometry("600x600")
app.title("Speech to text")

start_button = tk.Button(app, text="Start Recording", command=start_recording)
start_button.pack(pady=10)

stop_button = tk.Button(app, text="Stop Recording", command=stop_recording, state=tk.DISABLED)
stop_button.pack(pady=10)

status_label = tk.Label(app, text="Press 'Start Recording' to begin.")
status_label.pack(pady=10)

result_label = tk.Label(app, text="Transcription will appear here.")
result_label.pack(pady=10)

app.mainloop()
