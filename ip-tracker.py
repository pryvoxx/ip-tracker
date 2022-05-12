# Created by pryvox 
# description : Track ip 

# importer les modules nécaissaires 
import os 
import json 
import urllib.request as urllib2
from pystyle import Box, Colors, Colorate, Write 

# clear le terminal 
os.system('cls')
print(Colorate.Horizontal(Colors.yellow_to_red, """
████████ ██████   █████   ██████ ██   ██       ██ ██████  
   ██    ██   ██ ██   ██ ██      ██  ██        ██ ██   ██ 
   ██    ██████  ███████ ██      █████   █████ ██ ██████  
   ██    ██   ██ ██   ██ ██      ██  ██        ██ ██      
   ██    ██   ██ ██   ██  ██████ ██   ██       ██ ██                                                        
"""))
Write.Print("\n\nCreated by PRYVOX", Colors.red_to_yellow, interval=0.005)
# creation d'une boucle while 
while True: 
    ip = Write.Input("\n\nWhat is the ip adress of your victim ->", Colors.green_to_yellow, interval=0.05)
    url = "http://ip-api.com/json/"
    response = urllib2.urlopen(url + ip)
    data = response.read()
    info = json.loads(data)

    # afficher les resultats 
    Write.Print(f"---------------------------------\n", Colors.red_to_green, interval=0.0005)
    Write.Print(f"IP                :" + info['query'], Colors.red_to_green, interval=0.04)
    Write.Print(f"\nCountry         :" + info['country'], Colors.red_to_green, interval=0.04)
    Write.Print(f"\nCode Country    :" + info['countryCode'], Colors.red_to_green, interval=0.04)
    Write.Print(f"\nRegion          :" + info['region'],  Colors.red_to_green, interval=0.04)
    Write.Print(f"\nNom de region   :" + info['regionName'], Colors.red_to_green, interval=0.04)
    Write.Print(f"\nVille           :" + info['city'], Colors.red_to_green, interval=0.04)
    Write.Print(f"\nCode postale    :" + info['zip'], Colors.red_to_green, interval=0.04)
    Write.Print(f"\nZone            :" + info['timezone'], Colors.red_to_green, interval=0.04)
    Write.Print(f"\nOperateur wifi  :" + info['isp'], Colors.red_to_green, interval=0.04)
    break
