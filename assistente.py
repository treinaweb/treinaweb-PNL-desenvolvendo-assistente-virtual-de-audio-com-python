from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os
from datetime import datetime

def cria_audio(audio, mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(audio)
    playsound(audio)
    os.remove(audio)

def monitora_audio():
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Diga alguma coisa")
            audio = recon.listen(source)
            try:
                mensagem = recon.recognize_google(audio, language="pt-br")
                mensagem = mensagem.lower()
                print("Você disse ", mensagem)
                executa_comandos(mensagem)
                break
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                pass
        return mensagem


def executa_comandos(acao):
    if 'horas' in acao:
        hora = datetime.now().strftime("%H:%M")
        frase = f"Agora são{hora}"
        cria_audio("audio/mensagem.mp3", frase)
   
def main():
    while True:
        monitora_audio()

main()
