#barcode
from time import sleep
#opens the files for later use
file1 = open("cataloge.txt", "r+")
file2 = open("recipt.txt", "w")
#set finishedPrice as float (4 or 8 bytes)
finishedPrice = 0.00

#set reciptTop as str (1 byte per char)
#set reciptBottom as str (1 byte per char)
#defines the two varaiables 'reciptTop' and 'reciptBottom'[]
reciptTop = """
      ---- Babey Hardwears ----
            Working from 
      Litham school, School lane,
        That place, NR27 999
        Phone: 011h3i9m3999
      Operating Manager: N/A
            CEO: Jack B
------------------------------------------
Hardwear bought:

"""

reciptBottom = """

-------------------------------------------
      Thank you for your Custom
          Please shop agian
        Babey Hardwears LTD. 
      Owned by: Z0mbie INC. 🧟
-------------------------------------------
        Have a nice day 😊
"""
#reads 'file1' and puts its value into a variable
#set fileRead as list
fileRead = file1.readlines(0)
#set lineToWriteCat as list
lineToWriteCat = fileRead

def times(a):  
    #set newBarcode1 as int
    #set newBarcode2 as int
    #set newBarcode3 as int
    #set newBarcode4 as int
    #set newBarcode5 as int
    #set newBarcode6 as int
    #set newBarcode7 as int
    #puts each element of the string 'a' into a new variable
    newBarcode1 = int(a[0]) * 3
    newBarcode2 = int(a[1]) * 1
    newBarcode3 = int(a[2]) * 3
    newBarcode4 = int(a[3]) * 1
    newBarcode5 = int(a[4]) * 3
    newBarcode6 = int(a[5]) * 1
    newBarcode7 = int(a[6]) * 3
    #newBarcode8 = int(a[7]) * 1
    #creates the variable 'totalBarcode' as a global variable
    global totalBarcode
    #set totalBarcode as str (1 byte per char)
    #defines the variable totalBarcode
    totalBarcode = newBarcode1 + newBarcode2 + newBarcode3 + newBarcode4 + newBarcode5 + newBarcode6 + newBarcode7 #+ newBarcode8
    #outputs the 'totalBarcode' variable to the interactive window
    print(totalBarcode)
    #set remainder as int (2 or 4 bytes)
    #works out the remander (using the MODULUS operator) of 'totalBarcode' // 10
    remainder = totalBarcode % 10
    #sset lastDigit as int (2 or 4 bytes)
    #works out the last digit of the barcode 
    lastDigit = 10 - remainder
    #sets the 'barcodeFinal' variable as a global variable
    global barcodeFinal
    #set barcodeFinal as str (1 byte per char)
    #defines the variable 'barcodeFinal'
    barcodeFinal = a[0] + a[2] + a[3] + a[4] + a[5] + a[6] + str(lastDigit)
    #set totalBarcode2 as str (1 byte per char)
    #defines the variable ' totalBarcode2'
    totalBarcode2 = newBarcode1 + newBarcode2 + newBarcode3 + newBarcode4 + newBarcode5 + newBarcode6 + newBarcode7 + lastDigit
    #outputs barcodeFinal to the interactive window
    print(barcodeFinal)
    #sends 'totalBarcode2' to the valid procedure
    valid(totalBarcode2)

def valid(b):
    #set renainder_1 as int (2 or 4 bytes)
    #works out the remainder (using the MODULUS operator) of 'b' // 10
    remainder_1 = int(b) % 10
    #outputs 'b' to the interactive window
    print(b)
    if remainder_1 == 0:
        print("Valid")
    else:
        print("Not Valid")

def buy(barcode):
  #allows you to buy items from the store
    global finishedPrice
    global fileLine
    global lineToWriteCat
    print(barcode)
    print(str(fileRead))
    #checks to see what barcode you have entered
    if int(barcode) == int(fileRead[0]):
      #asks how many you want
      #set amount as int (2 or 4 bytes)
        amount = int(input("How many do you want? "))
        #looks to see if there is enough in stock
        if amount <= int(lineToWriteCat[3]):
          #if there is enough takes the amount away from the stock file
          #set newStock as int (2 or 4 bytes)
          newStock = int(lineToWriteCat[3]) - amount
          for x in range (len(lineToWriteCat)):
            if x == 3:
              print("No. 3")
              lineToWriteCat[x] = str(newStock) + "\n"
            else:
              lineToWriteCat[x] = lineToWriteCat[x]
              print(x)
        else:
          #if there isnt enough then tells the user
          print("Not Enough Stock")
          again()

        #adds the price times the amount to the current sub-total
        #set totalPrice as float (4 or 8 bytes)
        ##totalPrice = amount * float(fileRead[2])
        totalPrice = amount * float(0.50)
        #creates a variable to write to the recipt
        #set writeline as str (1 byte per char)
        writeline = fileRead[0] + "\t" + fileRead[1] + "\t" + str(amount) + "\t" + fileRead[2] + "\t" + str(round(totalPrice, 2))
        #writes the variable above to the recipt file
        file2.write(writeline)
        #adds the item sub-total to the overall sub-total
        finishedPrice += totalPrice
        #calls the again procedure
        again()
        #checks to see if it is this barcode the user has entered
    elif int(barcode) == int(fileRead[5]):
       #set amount as int (2 or 4 bytes)
        amount = int(input("How many do you want? "))

        if amount <= int(fileRead[8]):
          #if there is enough takes the amount away from the stock file
          #set newStock as int (2 or 4 bytes)
          newStock = int(lineToWriteCat[8]) - amount
          #a loop that creates a variable to change the file to the new stock number
          for x in range (len(lineToWriteCat)):
            #if the line numeber = 8 then it writes the new stock in
            if x == 8:
              #outpus the number 8 to the screen
              print("No. 8")
              lineToWriteCat[x] = str(newStock) + "\n"
              #if the line numeber isn't 8 then writes the current line again
            else:
              lineToWriteCat[x] = lineToWriteCat[x]
              #Outputs the line number to the screen
              print(x)
        else:
          #if there isnt enough then tells the user
          print("Not Enough Stock")
          #sends them to the 'again' procedure
          again()
        #Updates the total price using what is in the variable 'fileRead'
        #set totalPrice as float (4 or 8 bytes)
        totalPrice = amount * float(fileRead[7])
        #creates the variable 'writeline'
        #set writeline as str (1 byte per char)
        writeline = fileRead[5] + "\t" + fileRead[6] + "\t" + str(amount) + "\t" + fileRead[7] + "\t" + str(round(totalPrice, 2))
        #writes the variabel 'writeline' to 'file2'
        file2.write(writeline)
        #updates the 'finishedPrice' variable
        finishedPrice += totalPrice
        #sends the user to the 'again' procedure
        again()
    #checks to see if it is the barcode the user has eneterd
    elif int(barcode) == int(fileRead[10]):
      #asks the user how many of this product they want
      #set amount as int (2 or 4 bytes)
        amount = int(input("How many do you want? "))
        #check to see if there is enough stock
        if amount <= int(lineToWriteCat[13]):
          #if there is enough takes the amount away from the stock file
          #set newStock as int (2 or 4 bytes)
          newStock = int(lineToWriteCat[13]) - amount
          #updates the variable 'lineToWriteCat' to the new stock value, using a loop
          for x in range (len(lineToWriteCat)):
            #if the line number is 13:
            if x == 13:
              #output the line number
              print("No. 13")
              #makes that line the new stock value
              lineToWriteCat[x] = str(newStock) + "\n"
              #if the line number isn't 13
            else:
              #keeps the line the same
              lineToWriteCat[x] = lineToWriteCat[x]
              #prints the line number
              print(x)
        else:
          #if there isnt enough then tells the user
          print("Not Enough Stock")
          #send the user to the 'again' procedure
          again()
        #updates the 'totalPrice' variable
        #set totalPrice as float (4 or 8 bytes)
        totalPrice = amount * float(fileRead[12])
        #creates a line to write to a file
        #set writeline as str (1 byte per char)
        writeline = fileRead[10] + "\t" + fileRead[12] + "\t" + str(amount) + "\t" + fileRead[12] + "\t" + str(round(totalPrice, 2))
        #writes the variable 'writeline' to 'file2'
        file2.write(writeline)
        #updates the 'finishedPrice' variable
        finishedPrice += totalPrice
        #sends the user to the 'again' procedure
        again()
    else:
      #if the bacode dosent mach any of the database's barcodes it tells the user that the product cannot be found and writes it to the file
      #set writeline as str (1 byte per char)
        writeline = str(barcode) + "\t" + "product_not_found"
        #outputs that the barcode cannot be found
        print("Product not found")
        #calls the again procedure
        again()

#defines to 'stockAdd' procedure
def stockAdd():
  #gets the global variable fileRead
  global fileRead
  print(fileRead)
  file2.write(reciptTop)
  #asks the user for the barcode of the product they would like to add stock to
  #set barcodeAdd as int (2 or 4 bytes)
  barcodeAdd = str(input("Please enter the barcode of the product you would like to add stock for; "))
  #checks to see if the barcode is the same as element 0 in the 'fileRead' variable
  ##if barcodeAdd == str(fileRead[0]):
  #creates the variable 'lineToWriteAdd' as the same as 'fileRead' 
  #set lineToWriteAdd as list
  lineToWriteAdd = fileRead
  #asks the user how much they would like to add to the stock
  #set amountAdd as int (2 or 4 bytes)
  amountAdd = int(input("How much would you like to add? "))
  #adds "\n" onto the barcode so it can be compared
  barcodeAdd += "\n"
  print(barcodeAdd)
  #uses a loop to create a varibale to rewrite the file
  for x in range (len(lineToWriteAdd)):
    #if the line is line 0 then:
    if str(lineToWriteAdd[x]) == barcodeAdd:
       #creates the variable 'newStock' and assigns a value to it
      #set newStock as int (2 or 4 bytes)
      newStock = int(lineToWriteAdd[x+3]) + amountAdd
      #outputs "updated" to the interactive window
      print("Updated")
      #adds the new stock value to the variable
      lineToWriteAdd[x+3] = str(newStock) + "\n"
      #if the line number isn't 0 then:
    else:
      #add the current line to the variable 
      lineToWriteAdd[x] = lineToWriteAdd[x]
      #outputs the line numeber
      print(x)
  #asks the user if they want to add another product
  #set againAdd as int (2 or 4 bytes)
  againAdd = int(input("Do you want to add another product? (1 / 0) "))
  #if the variable 'againAdd' is 1:
  if againAdd == 1:
    #sends the user to the 'stockAdd'procedure
    stockAdd()
    #if the variable 'againAdd' is 0:
  elif againAdd == 0:
    #sends the user to the 'finished' procedure
    finished()
    #if the variable 'againAdd' is not 1 or 0:
  else:
    #output and error to the screen
    print("Not recoginsied finishing session")
    #sends the user to the 'finished' procedure
    finished()

#defines the 'again' procedure    
def again():
    #asks the user if they want to buy another product
    #set agian as str (1 byte per char)
    agian = str(input("Do you want to buy another product? "))
    #makes the input lower case so it can be selected properly
    agian.lower()
    #uses selection to find if the user entered 'yes' or 'no'
    if agian == "yes":
      #if the user inputed 'yes' then it sends the user to the 'startBuy' procedrue
        startBuy()
    elif agian == "no":
      #if the user inputed 'no' then it sends the user to the 'finished' procedure
        finished()
    else:
      #if nether 'yes' or 'no' is entered then it sends to to the start of the procedure
      print("Invalid Selection, please try again")
      again()
    
def startBuy():
    #asks the user to enter their 7 digit barocde to send to the 'buy' procedure
    #set barcode as str (1 byte per char)
    barcode = str(input("Enter your 7 number barcode: "))
    #writes the start of the recipt to 'file2' 
    file2.write(reciptTop)
    buy(barcode)
    
def startValid():
    #asks the user to enter their 7 digit barcode to send too the 'times' procedure
    #set barcode as str (1 byte per char)
    barcode = str(input("Enter your 7 number barcode: "))
    times(barcode)

def finished():
  #gets the variables 'finishedPrice' and 'lineToWriteCat' from a previous procedure
  global finishedPrice
  global lineToWriteCat
  #rounds the 'finishedPrice' variable to 2 decimal places
  #set finishedPrice as float (4 or 8 bytes)
  finishedPrice = round(finishedPrice, 2)
  #writes to 'file2' the recipt. 
  file2.write("\n")
  file2.write("\n")
  file2.write("Total cost of order                    ")
  file2.write(str(finishedPrice))
  file2.write(reciptBottom)
  #prints to the interactive window the final price
  print("Your total is: £", finishedPrice)
  print("Thanks for shopping with us")
  #adds lines to 'file2' so the next recipt is writen below the last one
  for x in range(1, 11):
      file2.write("\n")
  #closes the files
  file1.close()
  file2.close()
  #rewrites the cataloge with the 'lineToWriteCat' variable
  file1_1 = open("cataloge.txt", "w+")
  for x in range (len(lineToWriteCat)):
    file1_1.write(str(lineToWriteCat[x]))
    print(x)
  file1_1.close()
  print("END")
  
    
def menu():
  #for debuging
  #print(fileRead)
  #asks the user to input a numebr for selection
  #set choose as int (2 or 4 bytes)
  choose = int(input("Would you like to find a valid barcode(0) or buy some stuff(1) or add stock (2)? "))
  if choose == 0:
    #if the user enters '0' it sends them to the 'startValid' procedure
      startValid()
  elif choose == 1:
    #if the user enters '1' it sends them to the 'startBuy' procedure
     startBuy()
  elif choose == 2:
    #if the user enters '2' it sends them to the 'stockAdd' procedure
    stockAdd()
  else:
      #if a invalid number is entered then it retrys the procedure
      print("Error Unknown option entered please try again")
      menu()
      
def login():
  #Asks them what they want to do
  #set choose as int (2 ro 4 bytes)
  choose = str(input("Do you want to login (1) or create and account (2)"))
  #Recognises the input and makes a decision based on what they enter
  if choose == str(1):
    #if the user inputs no. 1 it calls the signIn procedure
    signIn()
  elif choose == str(2):
    #if the user input no. 2 it calls the signUp procedure
    signUp()
  elif choose == str(64):
    #if the user enter 64 (for devs only) it calls the menu procedure
    menu()
  else:
    #If the input is not 1 or 2 it asks them to make a valid input
    print("Not a recognised option please try again")
    login()

def signIn():
  #opens the file users.txt in the function of Read+
  usersRead = open("users.txt", "r+")
  #set usersReadLine as list
  usersReadLine = usersRead.readlines()
  #set usersReadLineTemp as str (1 byte per char)
  usersReadLineTemp = []
  ##print(usersReadLine)
  #asks the user to input their code
  #set loginCode as int (2 or 4 bytes)
  loginCode = str(input("What is your 4 digit code? "))
  #asks the user to input their username
  #set loginInUsername as str (1 byte per char)
  logInUsername = str(input("What is your username? "))
  #runs a loop for the number of lines in the file
  
  for x in range (len(usersReadLine)):
    #takes out the "\n"s
    usersReadLineTemp = usersReadLine[x].strip("\n")
    #takes out the "" in the list
    ##usersReadLineTemp = usersReadLineTemp[x].strip("")
    #makes usersReadLineTemp the same as the current usersReadLine
    ##usersReadLineTemp += usersReadLine[x]
    ##print(usersReadLineTemp)
    
    #splits the stirng into a list, back into usersReadLine
    usersReadLineTemp = usersReadLineTemp.split(" ")
    ##print(usersReadLineTemp)
    sleep(1)
    #runs a loop for the amount of elements in the file, counts up in 3s
    for counter in range (0, len(usersReadLine)):
      #sleep(1)
      #print(str(usersReadLineTemp[counter]))
      sleep(1)
      #if the code is correct it moves on to see if the username is correct as well
      if loginCode == str(usersReadLineTemp[counter]):
        print("Code Found")
        #if the username is correct moves it on to the signInPass() function
        if logInUsername == str(usersReadLineTemp[counter + 1]):
          print("Username Found")
          signInPass(usersReadLineTemp, logInUsername, counter)
      #if you can't find the username or the code on that line print the numeber the counter is on
      else:
        print(counter)
 
  
  #if the username isnt found it prints a message
  print("Username and code not found please try again")
  signIn()

def signInPass(usersReadLine, logInUsername, counter):
  #adds one to the counter variable
  counter += 2
  #gets the user to input their password
  #set password as str (1 byte per char)
  password = str(input("What is your password? "))
  ##adding "\n" to the password so the file reads it properly
  ##password += "\n"
  #checks to see if the password is the same as what is asigned to the username
  if password == usersReadLine[counter]:
    #if true tell the user and send them to the menu() function
    print("Password Accepted")
    print("Welcome,", logInUsername)
    menu()
  else:
    #if false try again
    print("Please Try Again")
    signInPass(usersReadLine, logInUsername, counter)

def signUp():
  #set SpecialSym as list
  specialSym =['$', '@', '#', '%', '!', '.', ',', '<', '>', '[', ']', '{', '}', '"', '£', '&', '*', '(', ')', '`', '¬', '-', '_', '+', '+', '?', '/', '|'] 
  #opens the file users.txt in the function append
  users = open("users.txt", "a")
  #Asks the user for a code to assign
  #set code as int (2 or 4 bytes)
  code = str(input("What is your 4-digit code going to be? "))
  #if the code is only decimal numbers
  if code.isdecimal():
    if len(code) != 4:
      #if the code isn't 4 digits:
      #output an error to the screen
      print("Please make your code 4-digits")
      #sends the user to the signUp procedure
      signUp()
  else: 
    #outputs an error to the screen
    print("Your code must be only numbers")
    #sends the user to the signUp procedure
    signUp()
  #Asks the user for a username
  #set username as str (1 byte per char)
  username = str(input("What is your username going to be? "))
  if len(username) < 6:
    #if the username is less than 6 characters:
    #outputs an error to the screen
    print("Username is not long enough, please try agin (at least 6 characters)")
    #sends the user back to the signUp procedure
    signUp()
  #asks the user for a password
  #set password as str (1 byte per char)
  password = str(input("What is your password? "))
  if len(password) < 8 or len(password) > 20:
    #if the password is less than 8 characters:
    #outputs an error to the screen
    print("Your password is not valid, please make it longer than 8 charactersand shorter than 20")
    #sends the user to the signUp procedure
    signUp()
    #checks to see if password has a numeber in it
  elif not any(char.isdigit() for char in password):
    #if password doesn't have a number in it:
    #output an error to the screen
    print("Password must contain a number")
    #send the user to the signUp procedure
    signUp()
    #checks to see if the password has an upper case letter in it
  elif not any(char.isupper() for char in password):
    #if password doesn't have an upper case letter in it:
    #output an error to the screen
    print("password must contain a capital letter")
    #send the user to the signUp procedure
    signUp()
    #checks to see if the password has any special characters in it using the specialSym variable
  elif not any(char in specialSym for char in password): 
    #if there isnt any special characters in password:
    #output an error to the screen
    print('Password should have at least one Special Symbol') 
    #sends the user back to the signUp procedure
    signUp()
  #confirms the password
  #set checkPword as str (1 byte per char)
  checkPword = str(input("Please Confirm your password "))
  #checks if the passwords are the same
  if password == checkPword:
    #if it is TRUE; write it to the users file
    #Casting the variable 'code' into a string
    #creates the variable 'lineToWrite' and assigns data to it
    #set lineToWrit as str (1 byte per char)
    lineToWrite = str(code) + " "+ username + " " + password + " " + "\n"
    #writes 'lineToWrite' to 'users'
    users.write(lineToWrite)
    #outputs that your account is set up
    print("Your account is all set up please contine to the SignIn page")
    #closes the file 'users'
    users.close()
    #sends the user to the signIn procedure
    signIn()
  elif password != checkPword:
    #if it is not the same it asks them to try agian
    print("Your passwords do not match, please try again")
    #sends the user to the 'signUp' procedure
    signUp()
  else:
    #shouldn't happen but is just in case
    print("Unknow Error has occured")
    #sends the user to the 'signUp' procedure
    signUp()

#calls the 'login' procedure
login()