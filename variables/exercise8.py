amount = 1000.00
one_year = amount * 1.05
two_years = one_year * 1.05
three_years = two_years * 1.05
four_years = three_years * 1.05
five_years = four_years * 1.05
balance = five_years
print(balance)  # my first attempt, long

balance = (1000.00 * 1.05 * 1.05 * 1.05
            * 1.05 * 1.05)   # quicker way, book solution
print(balance)