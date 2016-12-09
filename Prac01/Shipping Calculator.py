__author__ = 'jc449735'
Instruction = "Welcome to SS.\n input negative numbers to quit"
print(Instruction)
no_of_item = 1
while no_of_item > 0:
    no_of_item=float(input("enter the number of the items: "))
    cost= float(input("enter the price of the item: $ "))
    shipping_cost=no_of_item * cost
    if shipping_cost >=100:
        shipping_cost = shipping_cost - (0.1 * shipping_cost)
    print("you shipping cost is: $",shipping_cost)

