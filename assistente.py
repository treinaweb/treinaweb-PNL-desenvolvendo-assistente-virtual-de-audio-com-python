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

def ultimas_noticias():
    site = get('https://news.google.com/rss?gl=BR&hl=pt-BR&ceid=BR:pt-419')
    noticias = BeautifulSoup(site.text, 'html.parser')
    for item in noticias.findAll('item')[:5]:
        mensagem = item.title.text
        cria_audio("audio/,mensagem.mp3", mensagem)

def cotacao_moeda(moeda):
    if moeda == "Dólar":
        requisicao = get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
        cotacao = requisicao.json()
        nome = cotacao['USDBRL']['name']
        data = cotacao['USDBRL']['create_date']
        valor = cotacao['USDBRL']['bid']
        mensagem = f'Cotação do {nome} em {data} é {valor} reais'
        cria_audio("audio/mensagem.mp3", mensagem)
    elif moeda == "Euro":
        requisicao = get('https://economia.awesomeapi.com.br/json/last/EUR-BRL')
        cotacao = requisicao.json()
        nome = cotacao['EURBRL']['name']
        data = cotacao['EURBRL']['create_date']
        valor = cotacao['EURBRL']['bid']
        mensagem = f'Cotação do {nome} em {data} é {valor} reais'
        cria_audio("audio/mensagem.mp3", mensagem)
    elif moeda == "Bitcoin":
        requisicao = get('https://economia.awesomeapi.com.br/json/last/BTC-BRL')
        cotacao = requisicao.json()
        nome = cotacao['BTCBRL']['name']
        data = cotacao['BTCBRL']['create_date']
        valor = cotacao['BTCBRL']['bid']
        mensagem = f'Cotação do {nome} em {data} é {valor} reais'
        cria_audio("audio/mensagem.mp3", mensagem)



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
    elif 'notícias' in acao:
        ultimas_noticias()
    elif 'cotação' in acao and 'dólar' in acao:
        cotacao_moeda("Dólar")
    elif 'cotação' in acao and 'euro' in acao:
        cotacao_moeda("Euro")
    elif 'cotação' in acao and 'bitcoin' in acao:
        cotacao_moeda("Bitcoin")
   
def main():
    while True:
        monitora_audio()

main()
