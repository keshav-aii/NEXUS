import speech_recognition as sr
import time



recognizer = sr.Recognizer()



recognizer.pause_threshold = 0.8
recognizer.non_speaking_duration = 0.3
recognizer.dynamic_energy_threshold = True



microphone = sr.Microphone()



with microphone as source:

    print("Calibrating microphone...")

    recognizer.adjust_for_ambient_noise(
        source,
        duration=1
    )



def listen():


    try:


        with microphone as source:


            print("🎤 Listening...")


            audio = recognizer.listen(

                source,

                timeout=8,

                phrase_time_limit=5

            )



        text = recognizer.recognize_google(
            audio
        )



        print(
            f"Recognized: {text}"
        )



        return text.lower().strip()



    except sr.WaitTimeoutError:


        return ""



    except sr.UnknownValueError:


        return ""



    except Exception as e:


        print(
            "Voice error:",
            e
        )


        return ""