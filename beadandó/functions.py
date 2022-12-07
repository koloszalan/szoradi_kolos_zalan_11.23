from data import *
from os import system

filename='cipok.csv'
cimsor=''

def menu():
    system('cls')
    print('0 - Kilépés')    
    print('1 - Áruházban nyilvántartott cipők')
    print('2 - Akcióban résztvevő cipők')
    print('3 - Cipők keresése márkanév alapján')
    print('4 - Státusz ellenőrzés')
    print('5 - Legdrágább cipőink')
    return input('Kérem válasszon az alábbi menüpontok közül: ')

def loadCipok():
    file=open(filename, 'r', encoding='utf-8')
    global cimsor
    cimsor=file.readline()
    for row in file:
        splitted=row.strip().split(';')
        nev.append(splitted[0])
        marka.append(splitted[1])
        akcio.append(splitted[2])
        raktaron.append(splitted[3])
        ar.append(splitted[4])
    file.close()

def printCipok():
    system('cls')
    print('Cipőink listája:\n')
    for i in range(0,len(nev)):
        print(f'\t{nev[i]}')
    input('Tovább...')

def printAkcios():
    system('cls')
    print('Akcióban résztvevő cipők')
    for i in range (len(akcio)):
        if akcio[i]=="Igen":
            print(f'\t{nev[i]}')
    input('Tovább...')
    
def markaKereses():
    system('cls')
    print('Márka alapján keresés')
    megadott=(input('\tAdja meg a keresni kívánt márka PONTOS nevét NAGYBETŰKKEL: '))
    for i in range(len(marka)):
        if marka[i]==megadott:
            print(f'\t{nev[i]}')
    input('Tovább...')

def printStatusz():
    system('cls')
    beirtnev=(input('\tAdja meg a keresni kívánt cipő PONTOS nevét NAGYBETŰKKEL: '))
    for i in range(len(nev)):
        if beirtnev==nev[i]:
            if raktaron[i]=="Igen":
                print('A megadott cipő van raktáron')
            if raktaron[i]=="Nem":
                print('A megadott cipő nincsen raktáron')
    input('Tovább...')

def printDraga():
    system('cls')
    maxpoz=0
    for i in range(len(ar)):
        if ar[i]>ar[maxpoz]:
            maxpoz=i
    print(f'{nev[maxpoz]} , {ar[maxpoz]} Ft')
    input('Tovább...')
