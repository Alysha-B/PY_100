digit = 4936          # Book answer as follows
ones = digit % 10
print(ones)

digit = digit // 10
tens = digit % 10
print(tens)

digit = digit // 10
hundreds = digit % 10
print(hundreds)

thousands = digit // 10
print(thousands)

print(" ")

digit_2 = 4936          # My first try as follows
ones_2 = digit_2 - 4930
print(ones_2)

tens_2 = (digit_2 - 4906) // 10
print(tens_2)

hundreds_2 = (digit_2 - 4036) // 100
print(hundreds_2)

thousands_2 = (digit_2 - 936) // 1000
print(thousands_2)