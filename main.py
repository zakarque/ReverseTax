import sys
import decimal
from termcolor import colored

def reTax(x,y):
    totalPrice = x - y
    print(colored('Total Price is ', 'white'), colored(x,'red'))
    print(colored('Discount by ', 'white'), colored(y,'blue'))
    x = decimal.Decimal(totalPrice/(1+0.07))
    y = decimal.Decimal(totalPrice - (totalPrice / (1 + 0.07)))
    print(colored('Price before tax is','yellow'), colored(x.quantize(decimal.Decimal('0.00')),'yellow', attrs=['bold', 'underline', 'blink']))
    print(colored('Tax is','yellow'),  colored(y.quantize(decimal.Decimal("0.00")),'yellow', attrs=['bold', 'underline', 'blink']))

i = 1
while i > 0:
    print("Want to know the Tax?")
    x = input("Enter Total Price (type 0 to exit): ")
    try:
        if float(x) > float(0):
            y = input("Do you have a Discount: ")
            try:
                if float(y) >= float(0):
                    try:
                        if float(x) - float(y) > float(0):
                            print('------------------------------')
                            print('------------------------------')
                            reTax(float(x),float(y))
                            print('------------------------------')
                            print('------------------------------')
                            print('---------NEXT QUESTION--------')
                            print('------------------------------')
                            print('------------------------------')
                        elif float(x) - float(y) <= float(0):
                            print('------------------------------')
                            print('Seems Like You Didn\'t Have To Pay')
                            print('------------------------------')
                        else:
                            i -= 1

                    except ValueError:
                        print('------------------------------')
                        print("Oops! That was no valid number.  Try again...")
                        print('------------------------------')
                else:
                    print('------------------------------')
                    print("Oops! That was no valid number.  Try again...")
                    print('------------------------------')

            except ValueError:
                print('------------------------------')
                print("Oops! That was no valid number.  Try again...")
                print('------------------------------')

        else:
            print('------------------------------')
            print("Oops! That was no valid number.  Try again...")
            print('------------------------------')

    except ValueError:
        print('------------------------------')
        print("Oops! That was no valid number.  Try again...")
        print('------------------------------')