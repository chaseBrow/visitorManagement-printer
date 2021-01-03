from win32com.client import Dispatch
import pathlib
import socket
import sys
import time
import os

def _generate_headers(response_code):
        header = ''
        if response_code == 200:
            header += 'HTTP/1.1 200 OK\n'
        elif response_code == 404:
            header += 'HTTP/1.1 404 Not Found\n'

        time_now = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
        header += 'Date: {now}\n'.format(now=time_now)
        header += 'Server: Printer-Server\n'
        header += 'Connection: close\n\n' # Signal that connection will be closed after completing the request
        return header

s = socket.socket()
host = 'localhost'
s.bind((host, 3080))
s.listen()

while True:
    c, addr = s.accept()
    while True:
        dat = c.recv(1024)
        if not dat:
            print("no data")
            break
        else:
            dat = dat.decode('utf-8')
            data = dat.split(':::')
            data = data[1].split('::')
            print(data[0])
            print(data[1])
            print(data[2])
            
        response_header = _generate_headers(200)
        response = response_header.encode()
        c.send(response)

        break


# name = "Chase Brown"
# access = "Escort Required"
# company = "Aunalytics"

# tag_path = pathlib.Path('./tag.label')

# printer_com = Dispatch('Dymo.DymoAddIn')
# my_printer = printer_com.GetDymoPrinters()
# printer_com.SelectPrinter(my_printer)

# printer_com.Open(tag_path)

# printer_label = Dispatch('Dymo.DymoLabels')

# printer_label.SetField('Access', access)
# printer_label.SetField('Name', name)
# printer_label.SetField('Company', company)

# printer_com.StartPrintJob()
# printer_com.Print(1, False)
# printer_com.EndPrintJob()