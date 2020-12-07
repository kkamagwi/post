# Диктуем аудио и превращаем в текст при помощи Python

'''
команды терминла
pip install SpeechRecognition

Далее устанавливаем зависимости исходя из оперционной системы

Windows
pip install pipwin
pip install PyAudio

Linux
sudo apt-get install portaudio19-dev python-pyaudio
pip install PyAudio

Mac
xcode-select --install
brew remove portaudio
brew install portaudio
pip3 install pyaudio
'''

import speech_recognition


sr = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Говорите, пожалуйста:  ")
    audio = sr.listen(source)

    try:
        print(sr.recognize_google(audio))
    except:
        print("Извините, но аудио не распознано")

# @endgmPythoOn
