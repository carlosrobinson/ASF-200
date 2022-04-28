product_description = input("Please enter the product description: ")
quatity = int(input(f"How many {product_description}es do you wish to purchase:  "))
items = float(quatity)
regular_price = input('What was the regular price: ')
if float(regular_price) > 19.00 and float(regular_price) < 39.00:
    discount = 0.15 * float(regular_price)
    price_per_item = float(regular_price) - discount
    final_price = "{:,.2f}".format(price_per_item)
    sales_tax = 0.065 * price_per_item
    total_price = price_per_item * quatity + round(sales_tax, 2)
    amount_saved = (float(regular_price) * items) - total_price + round(sales_tax, 2)
    overall_savings = "{:,.2f}".format(amount_saved)
    purchase_price = "{:,.2f}".format(total_price)
    print(f"\nYour Receipt \n-------------------\n{quatity} {product_description}es @ ${final_price} \nSales Tax ${round(sales_tax, 2)}\nTotal Amount Due ${purchase_price}\nAmount Saved ${overall_savings}")
elif float(regular_price) > 39.00:
    discount = 0.25 * float(regular_price)
    price_per_item = float(regular_price) - discount
    final_price = "{:,.2f}".format(price_per_item)
    sales_tax = 0.065 * price_per_item
    total_price = price_per_item * quatity + round(sales_tax, 2)
    amount_saved = (float(regular_price) * items) - total_price + round(sales_tax, 2)
    overall_savings = "{:,.2f}".format(amount_saved)
    purchase_price = "{:,.2f}".format(total_price)
    print(f"\nYour Receipt \n-------------------\n{quatity} {product_description}es @ ${final_price} \nSales Tax ${round(sales_tax, 2)}\nTotal Amount Due ${purchase_price}\nAmount Saved ${overall_savings}")
else:
    sales_tax = 0.065 * float(regular_price)
    total_price = float(regular_price) * quatity + round(sales_tax, 2)
    print(f"\nYour Receipt \n-------------------\n{quatity} {product_description}es @ ${regular_price} \nSales Tax ${round(sales_tax, 2)}\nTotal Amount Due ${total_price}")