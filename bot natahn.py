from distutils.cmd import Command
from doctest import testfile
import string
from turtle import st
import telebot
import time
import requests
from selenium import webdriver
from telebot import types
import threading

CHAVE_API = "6179501890:AAGhcDfAD1mmwtcHs9YXqjtrsxTHTA7Ybu0"

bot = telebot.TeleBot(CHAVE_API)

autorizar = 1
fluxo = {}

texto3 = """

Olá 👋 
Cansado de pagar caro em salas de sinais que não dão resultado? 

Tenho a solução para você! 
E o melhor totalmente Grátis 🫡✅

Ter acesso a um aplicativo desenvolvido por 4 hackers, lives operando ao vivo e poder recuperar todo dinheiro ja perdido com essas casas de apostas faz sentido para você?

Para ter acesso ao aplicativo é necessário você fazer cadastro na plataforma, através desse link que eu vou deixar aqui abaixo 👇

faz o cadastro e mande "ok"  👇"""

texto4 = """
Maravilha👏 

🚨 LEIA COM ATENÇÃO AGORA 🚨

Agora eu preciso que você deposite pelo menos o minimo que é R$50 reais para poder pegar os sinais dos hackers e multiplicar sua banca🤖 

Assim que depositar me envia aqui algum print ou algo do tipo, que após isso eu vou liberar o robô gratuito 

Observação 👇

👉 1°PASSO: Mande a FOTO que comprovete o seu deposito 

👉 2ºPASSO: E mande uma mensagem abaixo com a palavra "PRONTO"
"""

texto5 = """
Tudo pronto ✅

Agora clique nesse botão abaixo para acessar o canal onde vou liberar seu aplicativo 

Após acessar envie um Ok
"""




def enviar_mensagem_fixada(chat_id):
    # Texto da mensagem fixada
    mensagem_fixada = "Para vincular sua conta do aplicativo na casa de apostas, clique em /start👇"

    # Enviar a mensagem fixada
    bot.send_message(chat_id, mensagem_fixada, disable_notification=True, pin=True)

def verificar(mensagem):
    global fluxo
    moment = mensagem.text
    idchat = mensagem.chat.id
    print(moment)
    print(idchat)

    if fluxo.get(idchat) is None:
        fluxo[idchat] = 1

    if fluxo[idchat] == 1:
      
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton("Cadastrar", url="https://afiliadosb1.bet/redirect?referralCode=3D3535&mcode=cdfv")
        markup.add(button)
        bot.send_message(mensagem.chat.id, texto3, reply_markup=markup)
       
        fluxo[idchat] = 2

    elif fluxo[idchat] == 2:
        bot.send_message(mensagem.chat.id, texto4)
        fluxo[idchat] = 3

    elif fluxo[idchat] == 3:
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton("Acessar tutorial do aplicativo", url="https://t.me/reidossinaishack")
        markup.add(button)
        bot.send_message(mensagem.chat.id, texto5, reply_markup=markup)

        fluxo[idchat] = 0
         # Enviar mensagem para o chat específico
        chat_id_especifico = 5598054998
        mensagem_especifica = "Um usuário chegou ao final das mensagens."
        bot.send_message(chat_id_especifico, mensagem_especifica)

        segundo_usuario_chat_id = 1872761926
        mensagem_segundo_usuario = "Um usuário chegou ao final das mensagens ."
        bot.send_message(segundo_usuario_chat_id, mensagem_segundo_usuario)



    return True

    


@bot.message_handler(func=verificar)
def responder(mensagem):
    return True


def handle_messages(messages):
    for message in messages:
        bot.process_new_messages([message])


def poll_updates():
    bot.polling(none_stop=True, interval=0, timeout=10)


if __name__ == "__main__":
    update_thread = threading.Thread(target=poll_updates)
    update_thread.start()