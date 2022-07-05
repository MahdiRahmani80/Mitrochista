from .website import FARADARS,TOPLEARN
from instabot import Bot
from instagrapi import Client


# OUR DOMAIN
DOMAIN = "http://127.0.0.1:8000/"
# DOMAIN = "mitrochista.ir/"


# PUBLISHERS IDs
FARADARS_ID = "3f1a0bf7-fb4e-4510-bd9a-ae57d5d2ed36"
TOPLEARN_ID = "b4d94d07-1863-4e38-875c-6d389d29c134"


# LOGIN IN INSTAGRAM
def loginInsta():
    bot = Client()
    bot.login("mitrochista", "mahdi13800")

    return bot

    

def init():
    FARADARS.init(FARADARS_ID,DOMAIN, loginInsta())
    TOPLEARN.init(TOPLEARN_ID,DOMAIN, loginInsta())

