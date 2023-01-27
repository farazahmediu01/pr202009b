# Keyword Argument.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

def car(name,model,brand="Toyota"):
    """Display car information."""
    "Toyota 2000 altis"
    print(f"Car Name: {name}")
    print(f"Car Year: {model}")
    print(f"Car Company: {brand}")



def make_change(size,message):
    print(f"The message of shirt is {message}")


def full_name(first, last):
    name = f"{first} {last}"
    return name

describe_pet('dog', 'wille')
describe_pet('horse', 'jimmy')
describe_pet('cat', 'michel')
