numbers = [1,2,3]

total = 0

grand_total = 0

for num in numbers:
    total         = total + num
    grand_total   += num

print(total)
print(grand_total)

print(sum(numbers))