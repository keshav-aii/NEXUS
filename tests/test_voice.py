from voice.microphone import record
from voice.transcriber import transcribe

print("Speak...")

audio = record(5)

print("Transcribing...")

text = transcribe(audio)

print(text)