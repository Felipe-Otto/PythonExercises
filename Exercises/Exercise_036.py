house_value = int(input("Type the house's value: $"))
salary = float(input("Type the value of your salary: $"))
years = int(input("Type the quantity of years that you'll take to pay the house: "))
print("To pay a house of {} in {} years you'll need a loan of ${:.2f}.".format(house_value, years, house_value / (years * 12)))
print("The loan can be allowed!" if house_value / (years * 12) < salary * 0.3 else "The loan can't be allowed!")
