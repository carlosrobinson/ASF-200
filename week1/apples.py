#Apple price
applePrice = 0.50
#print(applePrice)
add_decimal = "{:.2f}".format(applePrice)
#print(add_decimal)

#User input
customers_name = input("Please enter your name: ")
#print(customers_name)
prompt = input("Hi " + customers_name + ". Apples cost $" +  add_decimal  + " each. How many do you wanna buy: ")
prompt2 = "Thank you "+ customers_name +  " for your purchase of " + prompt +  " apples at a cost of $" + add_decimal + " each."
print(prompt2)
