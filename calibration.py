from vosk import Model, KaldiRecognizer
import subprocess
import pyaudio

model = Model(r"C:\Users\sayoo\programming\python\vosk-model-small-en-us-0.15") #eng us lite
recognizer = KaldiRecognizer(model, 16000)

chunk = 8192

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=chunk)
stream.start_stream()

while True:
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        data = text[14:-3]
        print(data)
        filePath = "C://Users//sayoo//programming//python//YoutubeOpener//voicelog.txt"
        with open(filePath, 'a') as file:
            file.write(data)
            file.write("\n")
#press ctrl c to exit the calibration