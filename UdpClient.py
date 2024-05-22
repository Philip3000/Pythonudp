import time
import socket
import random
import datetime

PORT = 14014
PRODUCTNO = 8023

def send_sale_broadcast():
    #Opretter en socket hvor AF_INET betyder IPv4 og SOCK_DGRAM betyder UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    date = str(datetime.date)
    while True:
        #tilfældig int mellem 1-10
        sale_amount = random.randint(1, 10)
        #laver beskeden
        message = f'{PRODUCTNO}, {sale_amount}, '
        #Sender beskeden som broadcast type til den angivne port og indkoder beskeden
        s.sendto(message.encode(), ("<broadcast>", PORT))
        #venter i 1-3 sekunder
        time.sleep(random.randint(1, 3))


send_sale_broadcast()