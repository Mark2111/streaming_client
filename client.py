# -*- coding: utf-8 -*-
"""
Python music streaming client
"""
#Python3
###         mpg123 required, on linux 'apt-get install mpg123'

import requests,re, subprocess

def display(lista):
    subprocess.call("clear")
    print("Simple music client for command line")
    print("Playlist on the server")
    i = 1
    for each in lista:
        print("{0}. {1}".format(i, each))
        i+=1
    print("Enter q to exit.\n")
    
def player(inp):
    try:
        print("Playing...")
        print("Press Ctrl+c to stop")
        subprocess.call(["mpg123", "-q", (url + "/" + urls[inp-1])])
    except KeyboardInterrupt:
        print("Stopping...")
        

## Server ip, port
ip = str(input("Enter ip of your server:  "))
port = int(input("Enter port of your server:  "))
url = 'http://' + str(ip) + ':' + str(port)

## Getting page content
try:
    response = requests.get(url)
except:
    print("Server unreachable !")
    print("Closing app...")
    exit()
s = response.content.decode('utf-8')
urls = re.findall(r'href=[\'"]?([^\'" >]+)', s)

## Creating playlist from links
playlist = []
for each in urls:
    temp = re.sub(r'%20', " ", each)
    each = re.sub(r'%28', "\(", temp)
    temp = re.sub(r'%29', "\)", each)
    playlist.append(temp)
## Songs names in playlist list, links in urls list

## Starting the player
while True:
    display(playlist)
    inp = str(input("Input number of the song:  "))
    if inp == "q":
        break
    player(int(inp))
    
print("This is still under development by code_chief")