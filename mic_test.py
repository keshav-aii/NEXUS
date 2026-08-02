from voice.listener import listen

while True:
    text = listen()

    if text:
        print("You:", text)

        if text == "exit":
            break