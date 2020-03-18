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