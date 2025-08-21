expenses = [10.50, 8, 5, 15, 20, 5, 3]

t_sum = 0

for x in expenses:
    t_sum += x

total = sum(expenses)

print("You spent: ", t_sum)

print("You spent $", total, sep = '')
