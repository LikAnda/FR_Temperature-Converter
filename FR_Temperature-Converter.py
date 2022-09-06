import sys
import time

# definition de "slowPrint" utilisé pour le style
def slowPrint(s):
    for c in s :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

# fonction principale permettant de sélectionner le type de conversion
def main():
    slowPrint("\n#################[Covertisseur de Température]#################\n")
    slowPrint("\n[1] Calculer de degrés fahrenheit à degrés celsius\n[2] Calculer de degrés celsius à degrés fahrenheit")
    slowPrint("\n\nIndiquer le numéro souhaité: ")
    try:
        selection = int(input(''))
    except ValueError: #debug
        input("\nCe n'est pas un nombre.\nAppuyer sur entrer pour fermer le programme...")
        exit()
    
    if selection == 1:
        TfahrenheitToTclesius()
    if selection == 2:
        TcelsiusToTfahrenheit()
    elif selection != 1 and selection != 2: # debug
        input("\nCette option n'existe pas.\nAppuyer sur entrer pour fermer le programme...")
        exit()

# fonction permettant de calculer de degrés fahrenheit à degrés celsius
def TfahrenheitToTclesius():
    slowPrint("\nIndiquer le nombre de degrés fahrenheit: ")
    try:
        Tfahrenheit = int(input(''))
    except ValueError: # debug
        input("\nCe n'est pas un nombre.\nAppuyer sur entrer pour fermer le programme...")
        exit()

    Tcelsius = (Tfahrenheit - 32) * 5/9
    Tcelsius = round(Tcelsius, 1)

    slowPrint(f"La température de {Tfahrenheit}°F en degrés est de {Tcelsius}°C.\n")
    time.sleep(0.5)

# fonction premettant de claculer de degrés celsius à degrés fahrenheit
def TcelsiusToTfahrenheit():
    slowPrint("\nIndiquer le nombre de degrés celsius: ")
    try:
        Tcelsius = int(input(''))
    except ValueError: # debug
        input("\nCe n'est pas un nombre.\nAppuyer sur entrer pour fermer le programme...")
        exit()

    Tfahrenheit = (Tcelsius * 9/5) + 32
    Tfahrenheit = round(Tfahrenheit, 1)

    slowPrint(f"La température de {Tcelsius}°C en degrès fahrenheit est de {Tfahrenheit}°F\n")
    time.sleep(0.5)

# permet de répeter la boucle indéfiniment
while True:
    main()
