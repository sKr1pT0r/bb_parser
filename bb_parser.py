import socket
import os
import array
import pyfiglet
from colorama import Fore, init

def osclear():
    if your_os == '1':
        os.system('clear')
    elif your_os == '2':
        os.system('cls')
    else:
        exit()

def design_elements(element):
    if element == 1:
        print(Fore.LIGHTMAGENTA_EX + pyfiglet.figlet_format("BB_Parser", font="chunky") + Fore.RESET)
        print('=' * 60 + '\n')
    elif element == 2:
        print('=' * 60 + '\n')
    elif element == 3:
        print('\n' + '=' * 60 + '\n')

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(port_scan_delay)
    try:
        connect = sock.connect((ip, port))
        print(ip, Fore.LIGHTYELLOW_EX + '- Port 25565 is open' + Fore.RESET)
        successful_ips.append(ip)
        connect.close()
    except:
        pass

print('What are you using?')
print('1. Linux')
print('2. Windows')
your_os = input('Enter your OS: ')
osclear()

design_elements(1)
print('Example: 1.1.1.1-2.2.2.2')
ip_range = input('Enter Ip Range: ')
osclear()

design_elements(1)
print('Example: 1-65535')
port_range = input('Enter rort range: ')
osclear()

design_elements(1)
print('Example: 25565')
port_for_parsing = int(input('Enter the port for parsing: '))
osclear()

design_elements(1)
print('Recommended: 1, 0.5, 0.35, 0.25, 0.1, 0.05, 0.025, 0.0175')
port_scan_delay = float(input('Enter port scan delay: '))
osclear()

split_port_range = port_range.split('-')

starting_port = int(split_port_range[0])
end_port = int(split_port_range[1])

split_range_ip = ip_range.split('-')
starting_ip = split_range_ip[0]
end_ip = split_range_ip[1]

split_starting_ip = starting_ip.split('.')
split_end_ip = end_ip.split('.')

first_ip_element = int(split_starting_ip[0])
second_ip_element = int(split_starting_ip[1])
third_ip_element = int(split_starting_ip[2])
fourth_ip_element = int(split_starting_ip[3])

unsplit_ip = str(first_ip_element)+'.'+str(second_ip_element)+'.'+str(third_ip_element)+'.'+str(fourth_ip_element)

successful_ips = []

design_elements(1)

while unsplit_ip != end_ip:
    scan_port(unsplit_ip, port_for_parsing)

    if fourth_ip_element == 256:
        third_ip_element += 1
        fourth_ip_element = 0

    if third_ip_element == 256:
        second_ip_element += 1
        third_ip_element = 0

    if second_ip_element == 256 and first_ip_element <= 255:
        first_ip_element += 1
        second_ip_element = 0

    unsplit_ip = str(first_ip_element)+'.'+str(second_ip_element)+'.'+str(third_ip_element)+'.'+str(fourth_ip_element)

    fourth_ip_element += 1

processing_ip_number = 0
design_elements(3)

while processing_ip_number != len(successful_ips):
    port = int(starting_port)
    while port != end_port:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(port_scan_delay)
            connect = sock.connect((successful_ips[processing_ip_number], port))
            print(successful_ips[processing_ip_number], Fore.LIGHTGREEN_EX + '- Port', port, 'is open' + Fore.RESET)
            connect.close()
            port += 1
        except:
            port += 1
            pass
    processing_ip_number += 1
