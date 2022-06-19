from .website import FARADARS



# OUR DOMAIN
DOMAIN = "http://127.0.0.1:8000/"

# PUBLISHERS IDs
FARADARS_ID = "44ad1e47-6ffd-4345-b809-fc9fe86f395e"




def init():
    FARADARS.init(FARADARS_ID,DOMAIN)
