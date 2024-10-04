from vosk import Model, KaldiRecognizer
import subprocess
import pyaudio

youtube_url = "C://Users//sayoo//OneDrive//Desktop//YouTube.lnk"

model = Model(r"C:\Users\sayoo\programming\python\vosk-model-small-en-us-0.15") #eng us lite
recognizer = KaldiRecognizer(model, 16000)

chunk = 8192

wakeWord = []

youtubeData =  ["open you do",
                "often you do",
                "attorney you do",
                "up on you tube",
                "how can you do",
                "but when you do",
                "i've been doing",
                "can you do",
                "how can you do it",
                "how can you do",
                "i'm to do",
                "i'm new to it",
                "i'm going to do",
                "opening a job",
                "i'll bet you do",
                "what would you do",
                "open you do",
                "i've been you do",
                "can you do",
                "how can you do",
                "i've been you job",
                "opening",
                "i've been you do",
                "open you do",
                "open to me",
                "after you to me",
                "how can you do",
                "i do",
                "been to",
                "hopefully you do",
                "hopefully he will to"
                "open youtube",
                "open you to",
                "open yo do",
                "open youtube",
                "how can to me"]
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
        if data in youtubeData:
            subprocess.run(["start", "", youtube_url], shell=True)  # For Windows
            data = " "   
