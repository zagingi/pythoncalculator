import sys
def calculator():

    number1 = input('What is the first number? ')
    number2 = input('What is the second number? ')

    print ("your numbers are " + number1 + " and " + number2)

    addition = int(number1) + int(number2)
    subtraction = int(number1) - int(number2)
    multiplication = int(number1) * int(number2)
    division  = float(number1) / float(number2)

    print ("Addition = " + str(addition))
    print ("Subtraction = " + str(subtraction))
    print ("Multiplicaiton = " + str(multiplication))
    print ("Division = " + str(division))

    userInput = input('Press "y" to restart or anything else to exit!')

    if userInput == "y":
        calculator()

    else:
        sys.exit()
calculator()
