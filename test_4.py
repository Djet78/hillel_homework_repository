# ----------------------- task 4 ------------------------
# First variant

num = input("Enter your number, and program count all not even digits in it: ")
total = 0
for digit in num:
        if not int(digit) % 2 == 0:
            total += int(digit)
print(total)

# Second variant
num_2 = int(input("Enter your five digit number, and program count all not even digits in it: "))
total_2 = 0
if 1e4 <= num_2 <= 1e5 - 1:
    lst_of_digits = []
    lst_of_digits.append(num_2 // 10000)
    lst_of_digits.append((num_2 // 1000) % 10)
    lst_of_digits.append((num_2 // 100) % 10)
    lst_of_digits.append((num_2 // 10) % 10)
    lst_of_digits.append(num_2 % 10)
    for digit in lst_of_digits:
        if not digit % 2 == 0:
            total_2 += digit

print(total_2)
