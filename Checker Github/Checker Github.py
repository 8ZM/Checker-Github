import os

os.system('cls' if os.name == 'nt' else 'clear')
import random
from colored import fg
import requests
import sys
import sys as n
#tweakPy
import time as mm
import json
import time
import json
import secrets
from colorama import Fore, init

color3 = fg(2)
color1 = fg(1)
color2 = fg(50)
colooor = fg(1)
green_color = "\033[1;93m"
O = '\033[33m'  # orange
detect_color = "\033[m"
red_color = "\033[m"
end_banner_color = "\33[00m"
C = "\033[0m"
W = "\033[96m"
BRed="\033[1;31m"
Green="\033[0;36m"
Yellow="\033[0;33m"
count = 0
def slow(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 40)

banner = ('''
   _____ _ _   _           _        _____ _               _
  / ____(_) | | |         | |      / ____| |             | |
 | |  __ _| |_| |__  _   _| |__   | |    | |__   ___  ___| | _____ _ __
 | | |_ | | __| '_ \| | | | '_ \  | |    | '_ \ / _ \/ __| |/ / _ \ '__|
 | |__| | | |_| | | | |_| | |_) | | |____| | | |  __/ (__|   <  __/ |
  \_____|_|\__|_| |_|\__,_|_.__/   \_____|_| |_|\___|\___|_|\_\___|_|
 
                           Coded by @berlin.py
                       

''')
print(banner)

banner2 = """
   _____ _ _   _           _        _____ _               _
  / ____(_) | | |         | |      / ____| |             | |
 | |  __ _| |_| |__  _   _| |__   | |    | |__   ___  ___| | _____ _ __
 | | |_ | | __| '_ \| | | | '_ \  | |    | '_ \ / _ \/ __| |/ / _ \ '__|
 | |__| | | |_| | | | |_| | |_) | | |____| | | |  __/ (__|   <  __/ |
  \_____|_|\__|_| |_|\__,_|_.__/   \_____|_| |_|\___|\___|_|\_\___|_|


"""

time.sleep(1)

print(" ")

print(" ")

slow("- Github Checker ")

print(" ")

time.sleep(1)

username = 'user.txt'

use = username

file = open(username, "r")

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '_octo=GH1.1.757675268.1606661116; _device_id=f629b81e5083a13fa7ff014a68f146ad; tz=Asia%2FDubai; tz=Asia%2FDubai; user_session=1_webWJdC6-KCRvLPP8kCdYXseBBDeWd-uLbw5B1PN8iGaqg; __Host-user_session_same_site=1_webWJdC6-KCRvLPP8kCdYXseBBDeWd-uLbw5B1PN8iGaqg; logged_in=yes; dotcom_user=w89X; has_recent_activity=1; _gh_sess=EjdS347LjhnAHcdI%2B7aLQV9xGe0exyfegs3osnq3UdiDl8rOC8td4pKGZ%2Fp0qpn6xGlE2Apl2BuZgSYL9rUGuBHBzcJ%2Fi05RwIMeoWi%2BxGRWFWUeZp5O38PUCLx3sJ%2BYTJRxjs0NC84iYLcNpygCph5UNw2mHR4WD96F5jMTUNVj5wQH4ntWGHeAtvcDXF9h4sS1k4iLZ%2Bxj97PDOg8PpyhWTaOiQK7awdm2V9AGKcRsdhpkZ4Y5%2BtK1ytFCA9FlLUsshiHc2eBp8eE8kS03rhh1UeFgyeywoOJOYCID2cM%2BmYszXQxkAMbsGay8youvQzxL128%2B4kgG%2FCLX8insdoEZjsSxPFEge7F1myY5IBxDjeOui8skQfY3qjWQ1qWz%2Fpz4ort3tL8jfkN8H7ZYP3%2BL1n9AHayFw4ehNLlnJWyVSicbcxq7T1IqdpGrqiFHDTOhN%2Fg9A0zqK%2FLt%2FNAsplwVcRtwVMBsfynjEKVd3tYJXytFccDS3uGI1uUtahGYHspepz3gWL1tGuM88%2BsvBG6ao%2Bv1Jeg91LziNDgqrFzA4rTFdMHhLzhzBoaZXbK4w%2F4sUMZrz7QdSjJ7Cgy6E%2BkGzuAFX7Y9qyFPTa0b%2BO2flxg7oJIHAk%2B%2Bl0I4LC8fBXeT0q2th6mzki%2F3oqS38AL1ZRDm8hTZhzAv%2FvNc7amwOHCjveVnU1N0rfEOPHyX24JF3clZggLB0ptgfcFmkW9u%2FlBNDAZSOzwjXG5l6a18TV%2FtR6HoX2V5tViSqspjpurMiE2%2F7oWKoMWDa6eZe89o9QMtuj2FDi1txY18WbSlJmfUSSfERCvzL00KyVgj47l00bPFtgD7y2WkGFEYO2S9CTMkvX2P6og2igbY5LRqL94K9cEXd5vTvdLMF3cp%2FMgCXGQ%2FmRwPYIVRmQRlzySV1%2FgaMVufn46k05Ubvl%2FmqPWr0A2BNfHARB%2F%2F31w5OeQAHIKWTqSThMmuZ3D2BGRXVm0%2FnpnYl2XUW%2Fo%2BtApuJ9KRQYKngVHOg5vu0U6hJx58Z7i09cB9tKisIY8q43kFfK%2FHkOjwfSdzUEaiRO6vqOBYS1sSUyRUMiJdbijkdIfN7dQVaUNXeMbY--epk8IbZB8LCR3S32--4y%2FdnK2SoukkzGXhhv245Q%3D%3D',
    'if-none-match': 'W/"38bd103a9925fd49af948e551ca81125"',
    'referer': f'https://github.com/berliv',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

file = open(username, "r")

av = 0
tk = 0
er = 0
while True:
  user = file.readline().split('\n')[0]
  url = f'https://github.com/{user}'
  rq = requests.get(url, headers=headers)
  if (user == ""):
    print("")
    slow("- Done, Press Enter To Close Program ...")
    input("")
    exit(0)


  if rq.status_code == 404:
      av +=1
      os.system('cls' if os.name == 'nt' else 'clear')
      print(f'{banner2}\n- STARTING Check BY @berlin.py -\n\n=============================\n\n[-] Avilable : {av}\n\n[-] Taken : {tk}\n\n[-] Error : {er}\n\n=============================')
      with open('usersfound.txt', 'a') as x:
             x.write(user + '\n')
      

  elif rq.status_code == 200:
      tk +=1
      os.system('cls' if os.name == 'nt' else 'clear')
      print(f'{banner2}\n- STARTING Check BY @berlin.py -\n\n=============================\n\n[-] Avilable : {av}\n\n[-] Taken : {tk}\n\n[-] Error : {er}\n\n=============================')


  else:
      er +=1
      print(f'{banner2}\n- STARTING Check BY @berlin.py -\n\n=============================\n\n[-] Avilable : {av}\n\n[-] Taken : {tk}\n\n[-] Error : {er}\n\n=============================')
