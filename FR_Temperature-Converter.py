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
    slowPrint("\n#################[Convertisseur de Température]#################\n")
    slowPrint("\nSélectionner votre type de degré à convertir:")
    slowPrint("\n[1] Degrés Celsius\n[2] Degrés Fahrenheit\n[3] Degrés Kelvin")

    # FIRST SELECTION

    slowPrint("\n\nIndiquer le numéro souhaité: ")
    try:
        global firstSelection
        firstSelection = int(input(''))
    except ValueError: #debug
        input("\nCe n'est pas un nombre.\nAppuyer sur entrer pour fermer le programme...")
        exit()
    
    if firstSelection == 1:
        slowPrint("Indiquer le nombre de degrès celsius: ")
        try:
            global celsiusToConvert
            celsiusToConvert = int(input(''))
        except ValueError: #debug
            input("\nCe n'est pas un nombre.\nAppuyer sur entrer pour fermer le programme...")
            exit()

    if firstSelection == 2:
        slowPrint("Indiquer le nombre de degrès fahrenheit: ")
        try:
            global fahrenheitToConvert
            fahrenheitToConvert = int(input(''))
        except ValueError: #debug
            input("\nCe n'est pas un nombre.\nAppuyer sur entrer pour fermer le programme...")
            exit()

    if firstSelection == 3:
        slowPrint("Indiquer le nombre de degrès kelvin: ")
        try:
            global kelvinToConvert
            kelvinToConvert = int(input(''))
        except ValueError: #debug
            input("\nCe n'est pas un nombre.\nAppuyer sur entrer pour fermer le programme...")
            exit()
        
    elif firstSelection != 1 and firstSelection != 2 and firstSelection != 3: # debug
        input("\nCette option n'existe pas.\nAppuyer sur entrer pour fermer le programme...")
        exit()
    
    
    # SECOND SELECTION
    
    slowPrint("\nSélctionner le type de degrès auquel convertir:")


    if firstSelection == 1:
        slowPrint("\n[1] Degrés Fahrenheit\n[2] Degrés Kelvin")
        slowPrint("\n\nIndiquer le numéro souhaité: ")
        try:
            secondSelection = int(input(''))
        except ValueError: #debug
            input("\nCe n'est pas un nombre.\nAppuyer sur entrer pour fermer le programme...")
            exit()
        if secondSelection == 1:
            convertToFahrenheit()
        if secondSelection == 2:
            convertToKelvin()
        elif secondSelection != 1 and secondSelection != 2:
            input("\nErreur.\nAppuyer sur entrer pour fermer le programme...")
            exit()
        
    if firstSelection == 2:
        slowPrint("\n[1] Degrés Celsius\n[2] Degrés Kelvin")
        slowPrint("\n\nIndiquer le numéro souhaité: ")
        try:
            secondSelection = int(input(''))
        except ValueError: #debug
            input("\nCe n'est pas un nombre.\nAppuyer sur entrer pour fermer le programme...")
            exit()
        if secondSelection == 1:
            convertToCelsius()
        if secondSelection == 2:
            convertToKelvin()
        elif secondSelection != 1 and secondSelection != 2:
            input("\nErreur.\nAppuyer sur entrer pour fermer le programme...")
            exit()

    if firstSelection == 3:
        slowPrint("\n[1] Degrés Celsius\n[2] Degrés Fahrenheit")
        slowPrint("\n\nIndiquer le numéro souhaité: ")
        try:
            secondSelection = int(input(''))
        except ValueError: #debug
            input("\nCe n'est pas un nombre.\nAppuyer sur entrer pour fermer le programme...")
            exit()
        if secondSelection == 1:
            convertToCelsius()
        if secondSelection == 2:
            convertToFahrenheit()
        elif secondSelection != 1 and secondSelection != 2:
            input("\nErreur.\nAppuyer sur entrer pour fermer le programme...")
            exit()    
    
    elif firstSelection != 1 and firstSelection != 2 and firstSelection != 3: # debug
        input("\nCette option n'existe pas.\nAppuyer sur entrer pour fermer le programme...")
        exit()

def convertToCelsius():
    if firstSelection == 1:
        finalConversion = (fahrenheitToConvert - 32) * 5/9
        finalConversion = round(finalConversion, 2)
        slowPrint(f"\nLa température de {fahrenheitToConvert}°F en degrés Celsius est de {finalConversion}°C.\n")
        time.sleep(1)
    elif firstSelection == 3:
        finalConversion = kelvinToConvert - 273.5
        finalConversion = round(finalConversion, 2)
        slowPrint(f"\nLa température de {kelvinToConvert} K en degrés Celsius est de {finalConversion}°C.\n")
        time.sleep(1)

# Convert To Fahrenheit
def convertToFahrenheit():
    if firstSelection == 1:
        finalConversion = (celsiusToConvert * 9/5) + 32
        finalConversion = round(finalConversion, 2)
        slowPrint(f"\nLa température de {celsiusToConvert}°C en degrés Fahrenheit est de {finalConversion}°F.\n")
        time.sleep(1)
    elif firstSelection == 3:
        finalConversion = (kelvinToConvert - 273.15) * 9/5 + 32
        finalConversion = round(finalConversion, 2)
        slowPrint(f"\nLa température de {kelvinToConvert} K en degrés Fahrenheit est de {finalConversion}°F.\n")
        time.sleep(1)

# Convert To Kelvin
def convertToKelvin():
    if firstSelection == 1:
        finalConversion = celsiusToConvert + 273.1
        finalConversion = round(finalConversion, 2)
        slowPrint(f"\nLa température de {celsiusToConvert}°C en degrés kelvin est de {finalConversion} K.\n")
        time.sleep(1)
    elif firstSelection == 2:
        finalConversion = (fahrenheitToConvert - 32) * 5/9 + 273.15
        finalConversion = round(finalConversion, 2)
    slowPrint(f"\nLa température de {fahrenheitToConvert}°F en degrés Kelvin est de {finalConversion} K.\n")
    time.sleep(1)

while True:
    main()

