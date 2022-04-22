from gtts import gTTS
from playsound import playsound


def speech_vocabs(vocab):
    print('speech is with language English')
    language = 'en'
    audio = 'speech.mp3'
    sp = gTTS(text=vocab, lang=language, slow=False)
    sp.save(audio)
    playsound(audio)
