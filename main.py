## Barcode Scanner
## Written in Python 3.12.4, it is compatabale with any Python version after Python 3.10
## Created and Licensed by Jack Babey

## Import Statements
# JSON Manipulation
import json


def main():
    ##catalogue = readCatFile()
    ##writeCatFile(catalogue)
    clearScreen()
    while True:
        menuChoice = outputMenu()
        match menuChoice:
            case 1:
                purchase()
            case 2:
                restock()
            case 3:
                barcodeValidation()
            case 4:
                return None
            case _:
                clearScreen()
                print("UNKNOWN ERROR HAS OCCURED")
 
## Menu Choices
# Purchasing Items
def purchase():
    print("Please scan or enter the barcode of the item you would like to purchase")
    barcode = input(">> ")
    if(barcode.isnumeric() != True):
        clearScreen()
        print("Submitted Barcode Must Be In Numeric Format")
        return None

    item = getItem(barcode)
    if(item == None):
        clearScreen()
        print("Item Doesn't Exist")
        return None
    
    print("There are " + item["Count"] + " left in stock")
    print("Please enter the quantity desired")
    count = input(">> ")
    if(count.isnumeric() != True):
        clearScreen()
        print("The Item Count Must be an Integer Number")
        return None
    elif(count > item["Count"]):
        clearScreen()
        print("There isn't enough stock of that item")
        return None

# Restock Items
def restock():
    return None

# Barcode Validation
def barcodeValidation():
    return None

## Item Manipulaton
def getItem(barcode):
    data = readCatFile()
    print(data)
    print(json.dumps(data))
    for i in data["Items"]:
        print(json.dumps(i))
        if(i["Barcode"] == barcode):
            return i
    return None

## Menu   
def outputMenu():
    print("""
          Please Choose From the Following Options:
          1) Buy A Product
          2) Restock Stock
          3) Barcode Validation
          4) Exit
          """)
    choice = input(">> ")
    if(validateMenuChoice(choice) == True):
        return int(choice)
    else:
        outputMenu()
        
def validateMenuChoice(value):
    if(not value.isnumeric()):
        clearScreen()
        print("Please enter an integer value")
        return False
    elif(int(value) > 4 or int(value) < 1):
        clearScreen()
        print("Please choose a valid menu option")
        return False
    else:
        return True

## File Manipulation  
def writeCatFile(toWrite):
    with open("catalogue.json", mode="w", encoding="utf-8") as catFile:
        json.dump(toWrite, catFile)
    return None
    
def readCatFile():
    with open("catalogue.json", mode="r", encoding="utf-8") as catFile:
        catData = json.load(catFile)
    return catData

## Screen Clearing
def clearScreen():
    for i in range(0, 100):
        print("\n")

## Main Call
main()
