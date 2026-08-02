import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True


def listen():

    with sr.Microphone() as source:

        print("🎤 Listening...")

        audio = recognizer.listen(
            source,
            timeout=5,
            phrase_time_limit=8
        )

    try:

        text = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        print("Recognized:", text)

        return text.lower()

    except sr.UnknownValueError:
        return ""

    except Exception as e:
        print(e)
        return ""