# HW 4, Search, Order, and Display Inventory Program, Alex Jimenez
# Function reads in data and stores it in inv
def populateInventory(inv):
    infile = open("inventory.txt", 'r')
    line = infile.readline().rstrip()
    while (line != ""):
        inv.append(line.split(','))
        line = infile.readline().rstrip()
    infile.close()
    sortIDs(inv)

# Functions displays options the users picks from and does input validation
def showMenu():
    print("1. Display Products")
    print("2. Search for Product")
    print("3. Order a Product")
    print("4. Exit")
    choice = int(input("Pick your choice 1-4: "))
    while (choice != 1 and choice != 2 and choice != 3 and choice != 4):
        print("Pick 1-4, try again")
        choice = int(input("Pick your choice 1-4: "))
    return choice

# Function displays products and formats the display
def displayProducts(inv):
    display = ['ID', 'Item', 'Color', 'Cost', '# Available']
    for i in range(len(display)):
        print(f'{display[i]:^8}', end='\t')
    print()
    for r in range(len(inv)):
        for c in range(len(inv[r])):
            print(f'{inv[r][c]:^8}', end='\t')
        print()

# Function does input validation to make sure 1, 2, or 3 is entered
def validSearch():
    c = int(input("Enter 1 to search by item, 2 by color, or 3 by cost: "))
    while (c != 1 and c != 2 and c != 3):
        print("Please enter 1, 2 or 3 next time.")
        c = int(input("Enter 1 to search by item, 2 by color, or 3 by cost: "))
    return c

# Function searches for users item input in inventory and displays its data
def choice1(inv, choice):
    value = input("Enter the item you wish to search by (lower case letters): ")
    categories = ['ID', 'Color', 'Cost', '# Available']
    for i in range(len(categories)):
        print(f'{categories[i]:^8}', end='\t')
    print()
    for i in range(len(inv)):
        if (inv[i][choice] == value):
            display = [inv[i][0], inv[i][2], inv[i][3], inv[i][4]]
            for i in range(len(display)):
                print(f'{display[i]:^8}', end='\t')
            print()

# Function searches for users color input in inventory and displays its data
def choice2(inv, choice):
    value = input("Enter the color you wish to search by (lower case letters): ")
    categories = ['ID', 'Item', 'Cost', '# Available']
    for i in range(len(categories)):
        print(f'{categories[i]:^8}', end='\t')
    print()
    for i in range(len(inv)):
        if (inv[i][choice] == value):
            display = [inv[i][0], inv[i][1], inv[i][3], inv[i][4]]
            for i in range(len(display)):
                print(f'{display[i]:^8}', end='\t')
            print()

# Function searches for users price input in inventory and displays its data
def choice3(inv):
    value = input("Enter the your highest price: ")
    categories = ['ID', 'Item', 'Color', '# Available']
    for i in range(len(categories)):
        print(f'{categories[i]:^8}', end='\t')
    print()
    for i in range(len(inv)):
        if (inv[i][3] <= value):
            display = [inv[i][0], inv[i][1], inv[i][2], inv[i][4]]
            for i in range(len(display)):
                print(f'{display[i]:^8}', end='\t')
            print()

# Functions determines if a search based on either color, item, or price is done
def searchProducts(inv):
    c = validSearch()
    if (c == 3):
        choice3(inv)
    elif (c == 2):
        choice2(inv, 2)
    else:
        choice1(inv, 1)

# Function orders products based on ID # and displays a final balance owed
def orderProducts(inv):
    total = 0
    yes_no = input("Enter a 1 if you wish to order or 0 to stop: ")
    while (yes_no != 0):
        itemID = int(input("Enter the items ID #: "))
        i = 0
        while (i < len(inv)):
            if (inv[i][0] == itemID):
                amount = int(input("Enter the quantity you wish to order: "))
                while (amount > int(inv[i][4])):
                    print("Too large of an order pick", inv[i][4], "or less")
                    amount = int(input("Enter the quantity you wish to order: "))
                inv[i][4] = int(inv[i][4]) - amount
                total = total + float(inv[i][3]) * amount
            i = i + 1
        print("Your total is:", format(total, ".2f"))
        yes_no = int(input("Enter a 1 if you wish to order or 0 to stop: "))

# Function sorts the data in the data file from smallest ID # to greatest ID #
def sortIDs(inv):
    for i in range(len(inv) - 1):
        for j in range(i + 1, len(inv)):
            if (inv[i][0] > inv[j][0]):
                storage = inv[i]
                inv[i] = inv[j]
                inv[j] = storage
                """
                storage = inv[i][0]
                inv[i][0] = inv[j][0]
                inv[j][0] = storage

                storage = inv[i][1]
                inv[i][1] = inv[j][1]
                inv[j][1] = storage

                storage = inv[i][2]
                inv[i][2] = inv[j][2]
                inv[j][2] = storage

                storage = inv[i][3]
                inv[i][3] = inv[j][3]
                inv[j][3] = storage

                storage = inv[i][4]
                inv[i][4] = inv[j][4]
                inv[j][4] = storage
                """

# Function main creates the 2 dimensional list inv and calls other functions
def main():
    inventory = []
    populateInventory(inventory)
    choice = showMenu()
    while (choice != 4):
        if (choice == 1):
            displayProducts(inventory)
        elif (choice == 2):
            searchProducts(inventory)
        elif (choice == 3):
            orderProducts(inventory)
        else:
            print("Invalid choice")
        choice = showMenu()

# Call to main
main()