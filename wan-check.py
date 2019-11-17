#usr/bin/python3
# -*- coding: utf-8 -*-
#Importation de modules utilise
import os
import time

#Definition des variables
hostname = "www.google.fr" #Adresse de la machine sur laquel faire un ping
temps = 60 #Duree entre chaque ping

def ping() :
        reponse = os.system("ping -c 1 " + hostname + " > /dev/null 2>&1")
        if reponse == 0 :
                return 0
        else :
                return 1

def pingnok() :
        #URL notification par sms
        #print("Ping NOK je fais un sms")
        while ping() != 0 :
                time.sleep(temps)
                ping()
        #URL notification par sms
        #print("Ping OK je fais un sms")
        time.sleep(temps)
        programme()

def programme() :
        ping()
        if ping() == 0 :
                #print("Ping OK")
                time.sleep(temps)
                programme()
        else :
                #print("Ping NOK")
                pingnok()

#Programme
#print("Demarrage du programme de verification du ping")
#Si tu veux un sms lors du demarrage du programme mettre la commande curl en dessous
#URL notification par sms
programme()
