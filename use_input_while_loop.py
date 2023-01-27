def multiply(n1, n2):
    return str(n1 * n2)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def div(n1, n2):
    return n1 / n2
 
def describe_pet(animal_type,pet_name):
    """Display information about a pet."""
print(f"\nI have a {animal_type}.")
print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
