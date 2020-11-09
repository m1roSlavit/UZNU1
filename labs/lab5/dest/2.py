number = int(input("number: "))
number_copy = number
res = 0

length_counter = 0

sum_of_digits = 0
while(number >= 1):
    ost = number % 10
    number = int(number/10)
    sum_of_digits += ost
    length_counter += 1
    print(ost)

number_avg_val = sum_of_digits/length_counter
amount_of_digit_counter = 0

i_c = 0
while(number_copy >= 1):
    ost = number_copy % 10
    number_copy = int(number_copy / 10)
    if ost < number_avg_val:
        amount_of_digit_counter += 1
    i_c += 1



print("Result: ", amount_of_digit_counter)
