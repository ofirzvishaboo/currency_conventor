import functions
import subprocess
from ILS import ILS
from EUR import EUR
from USD import USD
import time


now = time.strftime("%d  %b - %Y %H:%M:%S ")
print("It is", now)

def get_user_value():
    restart = True

    while restart:
        user_choice = input("1 - USD to ILS / 2 - ILS to USD / 3 - EUR to ILS: ")
        try:
            if user_choice == "1":
                try:
                    value_to_convert = float(input("Enter quantity to convert: "))
                    usd = USD()
                    result = usd.calculate(value_to_convert)
                    print(result)
                    return result, usd.get_value(), "USD to ILS", value_to_convert
                except ValueError:
                    print("wrong input")
            elif user_choice == "2":
                try:
                    value_to_convert = float(input("Enter quantity to convert: "))
                    ils = ILS()
                    result = ils.calculate(value_to_convert)
                    print(result)
                    return result, ils.get_value(), "ILS to USD", value_to_convert
                except ValueError:
                    print("wrong input")
            elif user_choice == "3":
                try:
                    value_to_convert = float(input("Enter quantity to convert: "))
                    eur = EUR()
                    result = eur.calculate(value_to_convert)
                    print(result)
                    return result, eur.get_value(), "ILS to EUR", value_to_convert
                except ValueError:
                    print("wrong input")
            else:
                print("wrong input")
                continue
        except ValueError:
            print("wrong input")

def main():
    restart = True
    mylist = []
    while restart:
        mylist.append(get_user_value())
        choice = input("Would you like to convert another value? (y/n): ")
        while choice not in ["y", "n"]:
            choice = input("Invalid choice. Please enter 'y' to convert another value or 'n' to stop: ")
        if choice == "y":
            continue
        elif choice == "n":
            print("Thanks for using our currency converter")
            restart = False

    for lists in mylist:
        print(lists[0])
    functions.write_data(mylist)
    subprocess.run(["open", "alldata.txt"])  # Opening the CSV file


main()
