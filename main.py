from ReverseTax import reTax

i = 1
while i > 0:
    print("Want to know the Tax?")
    x = input("Enter Total Price (type 0 to exit): ")
    if int(x) == 0:
        print("Bye Bye!")
        break 
    else:
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