## Barcode Scanner
## Written in Python 3.9.13
## Created and Licensed by Jack Babey

## Import Statements
# JSON Manipulation
import json


def main():
    ##catalogue = readCatFile()
    ##writeCatFile(catalogue)
    menuChoice = outputMenu()
    match menuChoice:
        case 1:
            purchase()
        case 2:
            refill()
        case 3:
            barcodeValidation()
        case _:
            print("UNKNOWN ERROR HAS OCCURED")
    return None
    
def outputMenu():
    print("""
          Please Choose From the Following Options:
          1) Buy A Product
          2) Refill Stock
          3) Barcode Validation
          """)
    choice = input(">> ")
    if(validateMenuChoice(choice) == True):
        return choice
    else:
        outputMenu()
        
def validateMenuChoice(value):
    if(not value.isnumeric()):
        clearScreen()
        print("Please enter an integer value")
        return False
    elif(int(value) > 3 or int(value) < 1):
        clearScreen()
        print("Please choose a valid menu option")
        return False
    else:
        return True
    
def writeCatFile(toWrite):
    with open("catalogue.json", mode="w", encoding="utf-8") as catFile:
        json.dump(toWrite, catFile)
    return None
    
def readCatFile():
    with open("catalogue.json", mode="r", encoding="utf-8") as catFile:
        catData = json.load(catFile)
    return catData

def clearScreen():
    for i in range(0, 100):
        print("\n")

## Main Call
main()
