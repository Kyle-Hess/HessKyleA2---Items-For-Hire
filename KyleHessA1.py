'''
Kyle Hess, 10/4/2016
Details:
Items for hire is a simple program that allows the user to hire, return and add items.
Upon quiting the program the users modifications will be written to a csv file.

Github link: https://github.com/Kyle-Hess/KyleHess--Items-For-Hire
'''
import csv

# Menu Constant
MENU = "\nMenu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item\n(Q)uit"
itemsList = []


# Function Main runs the menu and writes the list back to file when user quits
def main():
    print("Items for hire - by Kyle Hess")
    load_items()
    with open("items.csv") as f:
        print(len(f.readlines()), "Items loaded from items.csv")
    print(MENU)

    choice = input("Enter Choice: ").upper()
    while choice != "Q":
        if choice == "L":
            listing_items()
        elif choice == "H":
            hiring_item()
        elif choice == "R":
            return_item()
        elif choice == "A":
            add_item()
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input("Enter Choice: ").upper()

    print("Thank you for using Items for hire ")
    with open("items.csv", "w", newline='') as csvfile:
        csv_out = csv.writer(csvfile, dialect='excel')
        for row in itemsList:
            csv_out.writerow(row)


######
'''
Pseudocode:
itemList = []
open file
search each line in the file
    item name
    description
    price
    hire
    itemList.append(itemname, description, price, hire)
close file
'''


# Loads the contents of the csv file
def load_items():
    items = open("items.csv", "r")
    # counter = 0
    for line in items:
        match = line.strip().split(",")
        name = match[0]
        description = match[1]
        price = match[2]
        hire = match[3]
        itemsList.append([match[0], match[1], match[2], match[3]])
        # mylist.append([counter, '=', match[0],'$' match[1], match[2], match[3]])
        # counter += 1
    items.close()


######
# Lists the items in the itemsList, and shows the * symbol for items out of stock.
def listing_items():
    print("* Indicates item is NOT in stock.")
    for is_star in itemsList:
        if is_star[3] == 'out':
            print('{0} ({1}) = ${2}*'.format(*is_star))
        else:
            print('{} ({}) = ${}'.format(*is_star))


######
'''
Pseudocode:
hire = input"Enter the item you want to hire:"
items = open("items.csv", "r")
     reader = csv.reader(items)
     for i, line in enumerate(reader):
         print('{} = {}'.format(i, line))
     for hire in mylist
    if i == hire
        itemname[3] == 'out'
    print mylist

items.close()
'''


# Works with the enumerate version, and no counter in load_items.
# Hires an item that is in, and then changes it to 'out'.
# For it to work user has to enter Full name of item.
def hiring_item():
    for hired_items in itemsList:
        if hired_items[3] == 'in':
            print('{} ({}) = ${}'.format( *hired_items))

    hire = str(input("Enter the Item you want to hire: "))
    for i, item_name in enumerate(itemsList):
        if item_name[0] == hire:
            temp = list(itemsList[i])
            temp[3] = "out"
            itemsList[i] = tuple(temp)
    if hire == '':
        print("Nothing was hired")
    else:
        print('{} | {} '.format(hire, "Has been hired"))


######
# Returns an item and changes the 'out' to 'in'
# Again have to enter full name of item.
# If no input is entered returns to menu.
def return_item():
    for return_items in itemsList:
        if return_items[3] == 'out':
            print('{}: {} ({}) = ${}'.format("Out Items", *return_items))

    returning = str(input("Enter the Item you want to Return: "))
    for i, item_name in enumerate(itemsList):
        if item_name[0] == returning:
            temp = list(itemsList[i])
            temp[3] = "in"
            itemsList[i] = tuple(temp)
    if returning == '':
        print("Nothing was returned")
    else:
        print('{} | {} '.format(returning, "Has now returned"))


######
# Adds a new item to the bottom of a list
def add_item():
    while True:
        itemName = input("Item Name: ")
        if itemName == '':
            print("Input can not be blank.")
        else:
            break
    print()

    while True:
        description = input("Description: ")
        if description == '':
            print("Input can not be blank.")
        else:
            break
    print()

    while True:
        try:
            price = int(input("Price per day: $"))
        except ValueError:
            print("Invalid input; enter valid number")
            continue
        if price < 0:
            print("Price must be >= $0")
            continue
        else:
            break

    itemsList.append([itemName, description, price, 'in'])
    print('{} ({}), ${} - {}'.format(itemName, description, price, "now available for hire."))


main()
