from Tts import Tts

speech = input("Enter your speech : ")

tts = Tts("tts.mp3", speech, "fr")
tts.play_music(0.7)