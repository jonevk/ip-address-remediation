from datetime import date
import re
from os import listdir
from os.path import isfile, join
import requests
import time
from utils import parsemac
from bs4 import BeautifulSoup

prefix = "https://api.macvendors.com/"

def sanitize(mac):
    char_list = ['-', ':', '.']
    new_mac =[]
    output = ''
    if char_list[0] in mac:
        new_mac = mac.split(str(char_list[0]))
        return new_mac.join()
    elif char_list[1] in mac:
        new_mac = mac.split(str(char_list[1]))
        return new_mac.join()
    elif char_list[2] in mac:
        new_mac = mac.split(str(char_list[2]))
        return new_mac.join()
    else:
        new_mac = new_mac
    return new_mac

def rejoinmac(lst):
    output = ''.join(lst)
    return output

def get_oui_name(mac):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    page = f'{prefix}{mac}'
    mypage = requests.get(page, headers=headers).text
    mysoup = BeautifulSoup(mypage, 'html.parser')
    time.sleep(1.1) #Prevents API slowdown
    return mysoup

if __name__ == '__main__':
    foo = get_oui_name('00013Eddeeff')
    print('Vendor Name: {}'.format(foo))
    foo2 = get_oui_name('F4CFE2')
    print('Vendor Name: {}'.format(foo2))
    foo3 = sanitize('00:01:3E:dd:ee:ff')
    print(f'Sanitized version of Mac {foo3}')
    print (f'String version: {rejoinmac(foo3)}')