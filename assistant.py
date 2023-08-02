import speech_recognition as sr
import openai

def listen_to_commands():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"User Command: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your command.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        return ""


# Set your GPT-3 API key
openai.api_key = "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"

def generate_code(command):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Code a python program that {command}",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
    )

    return response.choices[0].text.strip()
def main():
    print("Voice Assistant: Ready to code for you!")

    while True:
        user_command = listen_to_commands()
        if "exit" in user_command:
            print("Voice Assistant: Goodbye!")
            break

        if user_command:
            code_snippet = generate_code(user_command)
            print(f"Generated Code: {code_snippet}")

if __name__ == "__main__":
    main()
