# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

from speech_recognition import Recognizer, AudioFile

recognizer = Recognizer()

with AudioFile('chile.wav') as audio_file:
  audio = recognizer.record(audio_file)

text = recognizer.recognize_google(audio)
print(text)