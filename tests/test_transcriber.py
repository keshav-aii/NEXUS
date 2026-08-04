from voice.microphone import record
from voice.transcriber import transcribe

print("Speak...")

audio = record(5)

text = transcribe(audio)

print(text)