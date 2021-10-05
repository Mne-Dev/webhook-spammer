##################################
# Author: https://bit.ly/3mtI3dg
##################################
import requests as r
import pyfiglet
import os
import time as t

def ascii():
    title = pyfiglet.figlet_format('Webhook Spammer', font='slant')
    print(f'{title}')

def clearAndAscii():
    os.system('cls')
    ascii()

ascii()
link = input('Webhook linkini girin(ZORUNLU)\n')
clearAndAscii()
content = input('Spamlanacak metni girin(ZORUNLU)\n')
clearAndAscii()
uname = input('Webhook adını girin(ZORUNLU)\n')
clearAndAscii()
avatar = input('Resim url si girin(OPSİYONEL)\n')
clearAndAscii()
print('Spam başlıyor...')
t.sleep(2)

while True:
    request = r.post(link,data={
            'content': content,
            'username': uname,
            'avatar_url': avatar
        })
    if(request.status_code == 204):
        print('Spam başarılı')
    t.sleep(0.4)