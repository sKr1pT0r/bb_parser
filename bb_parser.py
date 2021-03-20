import socket
import os
import array
import pyfiglet 
from colorama import Fore, init

def osclear():
    if youros == '1':
        os.system('clear')
    elif youros == '2':
        os.system('cls')
    else:
        exit()

print('What are you using?')
print('1. Linux')
print('2. Windows')
youros = input('Enter Your OS: ')
osclear()
print(Fore.LIGHTMAGENTA_EX + pyfiglet.figlet_format("BB_Parser", font = "chunky") + Fore.RESET)
print('=' * 60 + '\n')
print('Example: 1.1.1.1-2.2.2.2')
iprange = input('Enter Ip Range: ')
osclear()
print(Fore.LIGHTMAGENTA_EX + pyfiglet.figlet_format("BB_Parser", font = "chunky") + Fore.RESET)
print('=' * 60 + '\n')
print('Example: 1-65535')
portrange = input('Enter Port Range: ')
osclear()
print(Fore.LIGHTMAGENTA_EX + pyfiglet.figlet_format("BB_Parser", font = "chunky") + Fore.RESET)
print('=' * 60 + '\n')
print('Example: 25565')
findport = int(input('Enter Find Port: '))
osclear()

portrangesplit = portrange.split('-')

startport = int(portrangesplit[0])
endport = int(portrangesplit[1])

iprangesplit = iprange.split('-')
startip = iprangesplit[0]
endip = iprangesplit[1]

startipsplit = startip.split('.')
endipsplit = endip.split('.')

element1 = int(startipsplit[0])
element2 = int(startipsplit[1])
element3 = int(startipsplit[2])
element4 = int(startipsplit[3])

unsplitip = str(element1) + '.' + str(element2) + '.' + str(element3) + '.' + str(element4)

successful_ips = []

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.017)
    try:
        connect = sock.connect((ip, port))
        print(ip, Fore.LIGHTYELLOW_EX + '- Port 25565 is open' + Fore.RESET)
        successful_ips.append(ip)
        connect.close()
    except:
        pass

print(Fore.LIGHTMAGENTA_EX + pyfiglet.figlet_format("BB_Parser", font = "chunky") + Fore.RESET)
print('=' * 60 + '\n')

while unsplitip != endip:
    scan_port(unsplitip, findport)

    if element4 == 256:
        element3 += 1
        element4 = 0

    if element3 == 256:
        element2 += 1
        element3 = 0

    if element2 == 256 and element1 < 256:
        element1 += 1
        element2 = 0

    unsplitip = str(element1) + '.' + str(element2) + '.' + str(element3) + '.' + str(element4)

    element4 += 1

si_num = 0
print('\n' + '=' * 60 + '\n')

while si_num != len(successful_ips):
    port = int(startport)
    while port != endport:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.017)
            connect = sock.connect((successful_ips[si_num], port))
            print(successful_ips[si_num], Fore.LIGHTGREEN_EX + '- Port', port, 'is open' + Fore.RESET)
            connect.close()
            port += 1
        except:
            port += 1
            pass
    si_num += 1