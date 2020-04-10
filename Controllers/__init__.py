from Controllers.LoggerController import LoggerController
import os
import pyrebase


firebaseConfig = {
    "apiKey": "AIzaSyC3PdwUqSBKAA6Wsq3oS4J01ny01ANmRrQ",
    "authDomain": "paduasplayer.firebaseapp.com",
    "databaseURL": "https://paduasplayer.firebaseio.com",
    "projectId": "paduasplayer",
    "storageBucket": "paduasplayer.appspot.com",
    "messagingSenderId": "588241417634",
    "appId": "1:588241417634:web:1e3114f5330869aeb42efb"
}

log_dir = os.path.abspath('../paduasplayer/log/')

firebase = pyrebase.initialize_app(firebaseConfig)

logger = LoggerController(log_dir)
