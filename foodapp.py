# CREATE A FOOD APP THAT ALLOWS USERS TO SEE THE MENU, ALSO USER CAN SELECT A MENU
# AND ALSO THE QUANTITY, AND GETS IS ORDER DETAILS AND TOTAL BILL

print(f'''
      ########################################
      ##         welcome to wole-chop        ##
      ##     Your number one fingerlick      ##
      #########################################

      Select A Menu
      --------------
''')

menu = {
    1: ('Rice',100),
    2: ('Beans',200),
    3: ('Bread',600),
    4: ('Yam',1200),
    5: ('Eba',1500),
    6: ('Egg',500),
}

order =[]
bill= 0
balance = int(input("Enter bal: "))
# function to display menu
def display_menu():
    for key,value in menu.items():
        print(f'{key}. {value[0]} - N {value[1]}')
    print(f'Current Balance : # {balance}')

while True:
    display_menu()
    try:
        choice = int(input('Select a food you want: '))
        quantity = int(input('Select the portion you want: '))
        print('\n')
    except:
        print(f'Invalid input, please enter a number: \n')
        continue

    if choice not in menu:
        print("Invalid choice, please select a valid number")
        continue

    food_name, price = menu[choice]
    cost = price * quantity
        
    if cost > balance:
        print("insufficient fund")
        print(f"Your balance is {balance}")
        continue
    else:
        balance  -= cost
        bill += cost
        order.append((food_name, quantity,price, cost))
        print(f'{food_name}, has been added to your order, with {quantity} portion x {price} = {cost}')

        if balance == 0:
            print("Your balance has been exhausted")
            break
        else:
            print(f'Your current balance is: #{balance}')
            order_gain = input('would you like to order again? (yes/no): ')
            if order_gain.lower() != 'yes':
                break
    
print('\n')
if not order:
    print('No order has been made')
else:
    print('''
        ---------------------------------------
        ##            YOUR ORDERS            ##
        ---------------------------------------
        ''')
for food_name,qty,price,cost in order:
    print(f'{food_name} - {qty} x #{price} = #{cost}')

print('''
        --------------YOUR BILL --------------
        ''')
print(f'Total Bill : #{bill}')


