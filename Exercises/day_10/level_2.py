#1
count_num = 1
sum_total = 0
for number in range(1, 101):
    sum_total += count_num
    count_num += 1
print("The sum of all numbers is", sum_total)
#2 
count_num = 1
sum_total_even = 0
sum_total_odd = 0
for number in range(1,101):
    if number % 2 == 0:
        sum_total_even += number
    else:
        sum_total_odd += number
print("The sum of all evens is", sum_total_even,". And the sum of all odds is", sum_total_odd)