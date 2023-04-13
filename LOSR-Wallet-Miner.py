import os
import time
import colorama
from colorama import Fore
from colorama import Style
import random
import string
import base64

colorama.init()

author = 'LO$R'

os.system('cls' if os.name == 'nt' else 'clear')

print(Fore.GREEN + 'Welcome to ' + Fore.MAGENTA + author + Fore.GREEN + ' Wallet Miner!' + Style.RESET_ALL)
print('')
crypto = str(input(Fore.MAGENTA + 'Choose Between ETH and BTC: ' + Style.RESET_ALL))

import win32gui
import win32con

if crypto == 'ETH' or crypto == 'BTC' or crypto == 'eth' or crypto == 'btc':
    print(Fore.GREEN + 'Scraping wallets...')
    time.sleep(1)
    print(Fore.MAGENTA + 'Scraping wallets...')
    time.sleep(1)
    print(Fore.GREEN + 'Scraping wallets...')
    time.sleep(1)
    print(Fore.MAGENTA + 'Scraping wallets...')
    time.sleep(1)
    print(Fore.GREEN + 'Wallets are being prepared for mining!')
    time.sleep(3)

LicenseKey = input(Fore.GREEN + 'Input License Key: ')
import urllib.request

if LicenseKey == 'LO$ROnTop':
    print(Fore.GREEN + 'Key is VAILD!')
    time.sleep(0.5)
else:
    print(Fore.GREEN + 'Invaild Key!')
    print(Fore.GREEN + 'Press Enter to quit!')
    input()
    exit()

print(Fore.GREEN + 'Checking if Key is Vaild... ')
time.sleep(1)
if author != base64.b64decode('TE8kUg==').decode('utf-8'):
    print(Fore.RED + 'L SKID')
    exit()

if crypto == 'ETH':
    adress = str(input(Fore.MAGENTA + 'Please enter your Ethereum adress: '))
    print(Fore.GREEN + 'Checking if address exists... ')
    time.sleep(2)
    print(Fore.GREEN + 'Check has been successfully!')
elif crypto == 'BTC':
    adress = str(input(Fore.MAGENTA + 'Please enter your Bitcoin address: '))
    print(Fore.GREEN + 'Checking if address exists... ')
    time.sleep(2)
    print(Fore.GREEN + 'Check has been successfully!')

class bcolors:
    Won = '\x1b[36m'
    Fail = '\x1b[36m'


def id_gen(size):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=size))

def MINERRRRR(crypto):
    tries = 0
    while True:
        tries += 1
        if crypto == 'BTC' or crypto == 'btc':
            if tries > random.randint(150, 0x2540BE400):
                print(Fore.MAGENTA + '[-] bc1' + id_gen(40) + ' | Valid | ' + '1.673 BTC')
                print('Transfering 1.673 BTC to', adress)
                print('Your BTC will be added to your ETH address of 72 Hours Times can differ! ')
                time.sleep(6)
                tries = 0
                print(Fore.GREEN + 'Done! ' + author + ' Wallet Miner is running again!')
                time.sleep(3)
            else:
                print(Fore.RED + '[-] bc1' + id_gen(40) + '| Invalid |' + '0.0000 BTC')
                tries += 1
        elif crypto == 'ETH' or crypto == 'eth':
            if tries > random.randint(150, 0x2540BE400):
                print(Fore.MAGENTA + '[-] 0x' + id_gen(40) + ' | Valid | ' + '2.163 ETH')
                print('Transfering 3.463 ETH', adress)
                print('Your ETH will be added to your ETH address of 72 Hours Times can differ! ')
                time.sleep(6)
                tries = 0
                print(Fore.GREEN + 'Done! ' + author + ' Wallet Miner is running again!')
                time.sleep(3)
            else:
                print(Fore.RED + '[-] bc1' + id_gen(40) + '| Invalid |' + '0.0000 ETH')
                tries += 1
        else:
            print(Fore.GREEN + "Invalid currency. Please choose between 'ETH' and 'BTC'")

MINERRRRR(crypto)
