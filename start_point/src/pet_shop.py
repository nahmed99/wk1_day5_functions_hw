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
    returned_pets = []

    # 'extract' list of pet dictionaries to work with
    pets = pet_shop["pets"]

    # loop through list of pet dictionaries to find matching breeds
    for pet in pets:
        if pet["breed"] == breed:
            returned_pets.append(pet)

    return returned_pets


def find_pet_by_name(pet_shop, name):

    # 'extract' list of pet dictionaries to work with
    pets = pet_shop["pets"]

    # create a variable of 'None' to return in event of not found
    return_name = None

    for pet in pets:
        if pet["name"] == name:
            # return the current pet dictionary!
            return pet 

    return return_name


def remove_pet_by_name(pet_shop, name):
    # use a slightly different method to access dictionaires than before
    pet_shop["pets"].remove(find_pet_by_name(pet_shop, name))


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, amount):
    customer["cash"] -= amount


def get_customer_pet_count(customer):
    return len(customer["pets"])
