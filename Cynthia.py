def getTotal(amount, amount_paid, VAT):
    balance = amount_paid - (amount * VAT)
    return balance


def userInput():

    amount = int(input("Enter the total amount to be paid: "))
    print("Total is: KES {0:.2f} ".format(amount)) 

    #Changed the variable name for sum to amount_paid
    amount_paid = int(input("\nEnter the amount paid:"))
    print("Amount paid is: KES {0:.2f} ".format(amount_paid))

    #Retrieve the VAT
    vat_float = float(input("\nEnter the TAX rate:"))
    print("VAT is: "+str(vat_float)+"% \n")

    #Convert the VAT rate to a percentage fraction
    vat = vat_float/100

    balance = getTotal(amount, amount_paid, vat)

    print("Your balance is: KES {0:.2f} ".format(balance))


userInput()
