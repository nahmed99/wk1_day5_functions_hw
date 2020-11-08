# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, sum):
    #Add (or subtract) sum from current total_cash
    pet_shop["admin"]["total_cash"] += sum


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, amount):
    pet_shop["admin"]["pets_sold"] += amount


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed):
    # create empty list
    return_pets = []

    # 'extract' list of pet dictionaries to work with
    pets = pet_shop["pets"]

    # loop through list of pet dictionaries to find matching breeds
    for pet in pets:
        if pet["breed"] == breed:
            return_pets.append(pet)

    return return_pets




