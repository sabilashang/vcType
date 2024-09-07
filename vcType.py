import speech_recognition as sr
import pyautogui

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Function to perform actions based on voice commands
def perform_action(command):
    if "type" in command:
        # Type the given text
        text = command.replace("type", "", 1).strip()
        pyautogui.typewrite(text)

    elif "delete the last word" in command:
        # Delete last word
        pyautogui.hotkey("ctrl", "backspace")

    elif "thank you for your service" in command:
        # Termination of Program
        print("Terminating...")
        exit()
        
# Function to listen for voice commands
def listen_for_commands():
    with sr.Microphone() as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("Command:", command)
        perform_action(command)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Loop to continuously listen for commands
while True:
    listen_for_commands()
