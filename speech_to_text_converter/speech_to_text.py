import time
import speech_recognition
from tqdm import tqdm

def record_voice():
    microphone = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as live_phone:
        microphone.adjust_for_ambient_noise(live_phone)
        print("I'm listening. Speak now!")
        time_start = time.time()
        progress_bar = tqdm(range(10), desc="Recording", unit="s")
        for i in progress_bar:
            time.sleep(1)
        progress_bar.close()
        audio = microphone.listen(live_phone, phrase_time_limit=10)
        time_end = time.time()
        time_elapsed = time_end - time_start
        print("Recording stopped after {:.2f} seconds".format(time_elapsed))
    try:
        answer = input("Would you like to record again? (y/n)")
        if answer == "y":
            return record_voice()
        else:
            phrase = microphone.recognize_google(audio, language='en')
            return phrase
    except speech_recognition.UnkownValueError:
        print("Sorry, I could not understand your speech.")
        answer = input("Would you like to record again? (y/n)")
        if answer == "y":
            return record_voice()
        else:
            return None

if __name__ == '__main__':
    phrase = record_voice()
    with open('recorded_text.txt','w') as file:
        file.write(phrase)
        print('the last sentence you spoke was saved in the file recorded_text.txt')

