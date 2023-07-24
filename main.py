import functions
import subprocess
from ILS import ILS
from EUR import EUR
from USD import USD
import time


now = time.strftime("%d  %b - %Y %H:%M:%S ")
print("It is", now)

def get_user_value():
    conversions = {
        "1": {"currency": USD(), "conversion_type": "USD to ILS"},
        "2": {"currency": ILS(), "conversion_type": "ILS to USD"},
        "3": {"currency": EUR(), "conversion_type": "ILS to EUR"}
    }

    while True:
        user_choice = input("1 - USD to ILS / 2 - ILS to USD / 3 - EUR to ILS: ")
        if user_choice in conversions:
            try:
                value_to_convert = float(input("Enter quantity to convert: "))
                currency = conversions[user_choice]["currency"]
                result = currency.calculate(value_to_convert)
                print(result)
                return result, currency.get_value(), conversions[user_choice]["conversion_type"], value_to_convert
            except ValueError:
                print("Invalid input")
        else:
            print("Invalid choice")


def main():
    restart = True
    mylist = []
    while restart:
        mylist.append(get_user_value())
        choice = input("Would you like to convert another value? (y/n): ")
        while choice not in ["y", "n"]:  # Keeping the user from making typo's
            choice = input("Invalid choice. Please enter 'y' to convert another value or 'n' to stop: ")
        if choice == "y":
            continue
        elif choice == "n":
            print("Thanks for using our currency converter")
            restart = False  # Breaks the while loops

    for lists in mylist:
        print(lists[0])  # Printing only the results
    functions.write_data(mylist)
    subprocess.run(["open", "alldata.txt"])  # Opening the Txt file


main()
