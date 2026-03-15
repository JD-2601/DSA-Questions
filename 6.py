# find item with minimum discount to avoid buying it.

n = int(input("Enter number of items:"))
 
min_discount = float("inf")
min_disc_item = ""

for i in range(1,n+1):
    name,price,discount = input("Enter item name, price and discount respectively:").split(",")
    price = int(price)
    discount = int(discount)

    discount_amount = price*discount/100
    if discount_amount<min_discount:
        min_discount = discount_amount
        min_disc_item = name

print("Item with minimum discount is:",min_disc_item)