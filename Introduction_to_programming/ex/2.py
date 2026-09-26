#1
def my_addresse():
    print("Juri Stoffer")
    print("Laubeckstrasse 2 3600 Thun")
    print("076 489 19 76")
#my_addresse()
    print("CS")

#2
def sales():
    sales = input("Enter the sales: ")
    profit = int(sales) * 0.23
    print("profit = " , profit)
#sales()

#3
def travel_time():
    speed = 70
    print(f"Distance traveled in 6 hours: {speed * 6} km")
    print(f"Distance traveled in 10 hours: {speed * 10} km")
    print(f"Distance traveled in 15 hours: {speed * 15} km")
#travel_time()

#4
def gas_used():
    miles = input("Enter the miles: ")
    miles = int(miles)
    gas_used = input("Enter the gas used: ")
    gas_used = int(gas_used)
    MGP = miles/gas_used
    print(MGP)


#gas_used()


#5
def converter():
    cel_temp = input("Enter the Temperature in Celsius: ")
    cel_temp = int(cel_temp)
    fah_temp = (9/5)*cel_temp+32
    print(fah_temp)
#converter()

#6
def ing_adjuster():
    amount_c = input("Amount of cookies you wish to make: ")
    amount_c = int(amount_c)
    sugar = 1.5/48
    butter = 1/48
    flour = 2.75/48

    sugar = sugar * amount_c
    butter = butter * amount_c
    flour = flour * amount_c
    print(f"You need {sugar} Cups of Sugar")
    print(f"You need {butter} cup of Butter")
    print(f"You need {flour} cups of flour")

#ing_adjuster()


import numpy as np
def math_testing():
    matrix = np.matrix('1 2; 2 4')
    return matrix



print(math_testing)
print(math_testing())





