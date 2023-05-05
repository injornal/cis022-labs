"""
LAB 2
Kostiantyn Babich, Hyunjong Shin
This assignment is to make a base class and derived classes and use them to perform several operations
"""

import currency, krone, soum


def main():
    soum_currency, krone_currency = soum.Soum(), krone.Krone()
    array_currency = [soum_currency, krone_currency]
    user_action = ''

    while True:
        soum_currency.print()
        krone_currency.print()

        raw_input = input()
        
        if raw_input == 'q':
            break
        
        array_input = raw_input.split()
        user_action = array_input[0]
        target_currency = array_input[1]
        amount = float(array_input[2])
        if array_input[3] == "Soum":
            new_currency_object = soum.Soum(amount)
        elif array_input[3] == "Krone":
            new_currency_object = krone.Krone(amount)
        
        if target_currency == 's':
            if user_action == 'a':
                array_currency[0].add(new_currency_object)
            elif user_action == 's':
                array_currency[0].subtract(new_currency_object)
            
        elif target_currency == 'k':
            if user_action == 'a':
                array_currency[1].add(new_currency_object)
            elif user_action == 's':
                array_currency[1].subtract(new_currency_object)




if __name__ == "__main__":
    main()
