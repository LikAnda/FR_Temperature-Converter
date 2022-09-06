import sys
import time

# definition de "slowPrint" utilisé pour le style
def slowPrint(s):
    for c in s :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

# definition de "separationPrint" utilisé pour le style (écrit le ligne de séparation plus rapidement)
def separationPrint(s):
     for c in s :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

# fonction principale permettant de sélectionner le type de conversion
def main():
    separationPrint("\n####################[LikAnda]###################\n")
    print("""\n[1] Calculer de degrés fahrenheit à degrés celsius
[2] Calculer de degrés celsius à degrés fahrenheit""")
    slowPrint("\nIndiquer le numéro souhaité: ")
    try:
        selection = int(input(''))
    except ValueError: #debug
        input("\nCe n'est pas un nombre.\nAppuyer sur entrer pour quitter le programme...")
        exit()
    
    if selection == 1:
        TfahrenheitToTclesius()
    if selection == 2:
        TcelsiusToTfahrenheit()
    else: # debug
        input("Erreur lors de la sélection. \nAppuyer sur entrer pour quitter le programme...")
        exit()

# fonction permettant de calculer de degrés fahrenheit à degrés celsius
def TfahrenheitToTclesius():
    slowPrint("\nIndiquer le nombre de degrés celsius: ")
    try:
        Tcelsius = int(input(''))
    except ValueError: # debug
        input("\nCe n'est pas un nombre.\nAppuyer sur entrer pour quitter le programme...")
        exit()

    Tfahrenheit = Tcelsius + 9/5 + 32
    Tfahrenheit = round(Tfahrenheit, 1)

    slowPrint(f"La température en fahrenheit de {Tcelsius}°C est de {Tfahrenheit}°F.\n\n")
    time.sleep(0.5)

# fonction premettant de claculer de degrés celsius à degrés fahrenheit
def TcelsiusToTfahrenheit():
    slowPrint("\nIndiquer le nombre de degrés fahrenheit: ")
    try:
        Tfahrenheit = int(input(''))
    except ValueError: # debug
        input("\nCe n'est pas un nombre.\nAppuyer sur entrer pour quitter le programme...")
        exit()

    Tcelsius = (Tfahrenheit - 32) + 5/9
    Tcelsius = round(Tcelsius, 1)

    slowPrint(f"La température en degrés de {Tfahrenheit}°F est de {Tcelsius}°C.\n\n")
    time.sleep(0.5)

# permet de répeter la boucle indéfiniment
while True:
    main()
