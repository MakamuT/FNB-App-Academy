foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press q to quit ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)
        
print("-------Your Cart-------")

for food, price in zip(foods, prices):
    print(f"{food}: R{price}")
    total += price

print("\n")
print(f"Your total is :R{total}")