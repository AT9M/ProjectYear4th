import speech_recognition as sr

#sudo apt-get install python-pyaudio python3-pyaudio




list_mic = sr.Microphone().list_microphone_names()



mic = sr.Microphone(device_index=n)   #N is PNP USB DEVICE


with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    
r.recognize_google(audio)