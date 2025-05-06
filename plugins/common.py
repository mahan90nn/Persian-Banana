import os, re
from colorama import Fore, Style
from plugins.logging import *
import time
from plugins.minecolor import parse

white = Fore.WHITE
yellow = Fore.YELLOW + Style.BRIGHT
red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT

clear = lambda: loadmenu(); print("\033c", end="")

# Checks if this is the first time that the user loaded banana
def firstload():

    if not os.path.exists("banana"): # Checks if file "banana" exists 
        with open("banana", "w") as f:
            f.write('') # Makes banana file
        return True
    
    # If banana exists will return False
    return False

def animate():
    print("\033c", end="")
    print(rf"""
{yellow}      ___                          
     / _ )___ ____  ___ ____  ___ _
    / _  / _ `/ _ \/ _ `/ _ \/ _ `/
   /____/\_,_/_//_/\_,_/_//_/\_,_/ {white}""")

    for i in range(19):
        line = "─" * i
        space = " " * (19 - i)
        print("\r" + space + line * 2, end="", flush=True)
        time.sleep(0.03)
    

# Loads the menu or something
def loadmenu():
    print("\033c", end="")
    print(rf'''
{yellow}      ___                          
     / _ )___ ____  ___ ____  ___ _
    / _  / _ `/ _ \/ _ `/ _ \/ _ `/
   /____/\_,_/_//_/\_,_/_//_/\_,_/ {white}
┣────────────────────────────────────┫
    {white}Dorod {os.getlogin()}. Kosh Omadi be {yellow}BANANA
    {white}benivs {yellow}help{white} ta command haro bebiny
    {white}Translated By Mr_Stable (@mahan90nn)
''')

# Checks if server domain is valid with regex
def checkserver(server):
    if ':' in server:
        server = server.split(':')[0]
    if server == 'localhost': return True
    ipre = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    domre = r'^(?:(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})$'

    if re.match(domre, server) or re.match(ipre, server):
        return True
    return False


def checkip(ip):

    ipre = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b' # ip regex
    if re.match(ipre, ip):
        return True

    return False
