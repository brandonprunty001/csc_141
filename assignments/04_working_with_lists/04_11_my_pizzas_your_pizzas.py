my_pizzas = ["pepperoni", "margherita", "bbq chicken"]
friend_pizzas = my_pizzas[:]  # make a copy of the list

my_pizzas.append("veggie")
friend_pizzas.append("hawaiian")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)