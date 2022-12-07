from functions import *
loadCipok()

choice=''
while choice!='0':
    choice=menu()
    if choice=='1':
        printCipok()
    if choice=='2':
        printAkcios()
    if choice=='3':
        markaKereses()
    if choice=='4':
        printStatusz()
    if choice=='5':
        printDraga()