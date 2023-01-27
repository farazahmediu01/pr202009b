from random import uniform, choice

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '@', '#', '$', '%',
           '^', '&', '*', '(', ')', '-', 'a', 'b', 'c', 'd', 'e']
password = ""


for num in range(8):
    random_index_int = int(uniform(0, len(numbers)))
    # random_index_int = choice(range(0, len(numbers)))
    letter = numbers[random_index_int]

    # if choice([0, 1]):
    #     letter = str(letter).upper()
    password += str(letter)

print(password)
