from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os
from datetime import datetime
import sys

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
    if 'fechar assistente' in acao:
        sys.exit()
    elif 'horas' in acao:
        hora = datetime.now().strftime("%H:%M")
        frase = f"Agora são{hora}"
        cria_audio("audio/mensagem.mp3", frase)
    elif 'desligar computador' in acao and 'uma hora' in acao:
        os.system("shutdown /s /t 3600")
    elif 'desligar computador' in acao and 'meia hora' in acao:
        os.system("shutdown /s /t 1800")
    elif 'cancelar desligamento' in acao:
        os.system("shutdown /a")
   
def main():
    while True:
        monitora_audio()

main()
