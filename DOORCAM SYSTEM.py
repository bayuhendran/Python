#Author Bayu Hendra Nugroho
#February, 28 2018
#1:00 PM
# Doorcam Telegram_bot

import sys
from picamera import PiCamera
from time import sleep
from gpiozero import Button
import telepot
import time, datetime
import os

button = Button(17)
camera = PiCamera()
camera.start_preview()
frame = 1

def handle(msg):
        chat_id = msg['chat']['id']
        command = msg['text']
        print 'Got command: %s' % command
    
        if command == '/ada':
                camera.stop_preview()
                print "Silakan masuk !"
                time.sleep(10)
                camera.start_preview()
        elif command == '/tidak_ada':
                camera.stop_preview()
                print " Silakan kembali di lain waktu !"
                time.sleep(10)
                camera.start_preview()
        elif command == '/hapus':
            os.system('rm /home/pi/Desktop/*')
            bot.sendMessage(chat_id, "Menghapus Semua Gambar")
        elif command == '/reg_1116':
            print chat_id
        elif command == '/matikan':
            camera.stop_preview();
        elif command == '/nyalakan':
            camera.start_preview();


def sorted_ls(path) :
            mtime = lambda f: os.stat(os.path.join(path, f)) .st_mtime
            return list(sorted(os.listdir(path), key=mtime))

# nyieun bot api euy
bot = telepot.Bot('502558410:AAH04U8iX7KnphfVQN4eoONFMhR8wXl8Dyk')
bot.message_loop(handle)
print ('Listening ...')


while 1:
    
        button.wait_for_press()
        camera.capture('/home/pi/Desktop/frame%03d.jpg' % frame)
        frame += 1
        print 'Photo'
        hasil = sorted_ls ('/home/ pi/Desktop/')
        '''Bayu'''
        bot.sendPhoto('410802563', open('/home/pi/Desktop/'+hasil[-1], "rb"), caption = "Ada Tamu")
        '''Namakamu'''
        time.sleep(0.1)
