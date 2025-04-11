def select_dish(foods, selected_food):
    if selected_food < 0 or selected_food >= len(foods):
        raise ValueError("Choice out of menu range.")
    print(f"Ah, {foods[selected_food]}! An excellent choice!")

def your_menu(foods):
    try:
        index = 1
        for dish in foods:
            print(f"{index}. {dish}")
            index += 1
    
        selected_choice = int(input("Your order number? "))
        select_dish(foods, selected_choice - 1)
    except ValueError:
        print("Please enter a number, not letters or symbols.")
    except IndexError as error:
        print(f"{error} was entered.")
        print("Next time try entering something on the menu!")
        print("That number is not on the menu. Try again.")
    

menu_items = [
    "Yakisoba",
    "Pho Tai Nam Gan",
    "Chile Verde",
    "Swiss & Mushroom Burger",
    "Saag Paneer",
]

your_menu(menu_items)
print("Yum!")