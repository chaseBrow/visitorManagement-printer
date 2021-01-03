import socket
import sys
import time
# import subprocess
import os

def _generate_headers(response_code):
        header = ''
        if response_code == 200:
            header += 'HTTP/1.1 200 OK\n'
        elif response_code == 404:
            header += 'HTTP/1.1 404 Not Found\n'

        time_now = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
        header += 'Date: {now}\n'.format(now=time_now)
        header += 'Server: Simple-Python-Server\n'
        header += 'Connection: close\n\n' # Signal that connection will be closed after completing the request
        return header

file = open('label.label', 'r')
labelO = file.read()
file.close()

s = socket.socket()
host = 'localhost'
s.bind((host, 3080))

s.listen()

while True:
    c, addr = s.accept()
    while True:
        # lpr =  subprocess.Popen("/usr/bin/lpr -o landscape", stdin=subprocess.PIPE)
        label = labelO
        dat = c.recv(1024)
        if not dat:
            print("no data")
            break;
        else:
            dat = dat.decode('utf-8')
            data = dat.split(':::')
            data = data[1].split('::')
            # label = open('label.txt', 'r')
            label = label.replace('VAR_NAME', data[0])
            label = label.replace('VAR_COMPANY', data[1])
            label = label.replace('VAR_ACCESS', data[2])
            print(type(label))
            label = bytes(bytearray(label, encoding = 'utf-8'))
            print(label)
            os.system('lp -o lpi=2 -o landscape -o page-top=20 -o cpi=7 "headshot.png"')
            # lpr.stdin.write(b'')
            # lpr.stdin.close()

        response_header = _generate_headers(200)
        response = response_header.encode()
        c.send(response)

        break;
