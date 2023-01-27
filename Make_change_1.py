# Variable 'notes' contain all possible Banknotes and coins in Pakistani currency.
PKR = (1000, 500, 100, 50, 20, 10, 5, 2, 1)

# make_change contain the logic part.
def make_change(inp):
    for note in PKR:

        if inp // note != 0:
            print(f"{note}\t=\t{(inp // note)}")
        
        inp = inp % note


print("Progarm starts press 'e' to exit.")
while True:
    inp = input("\nEnter amount in Rupees: ")
    
    if inp.lower() == 'e':
        break
    try:
        inp = int(inp)

    except:
        print("\nEnter numbers only")
        print("\nPress 'e' to Exit. ")
        continue


    make_change(inp)
    print("-"*50)
    