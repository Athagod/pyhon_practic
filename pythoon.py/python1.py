def add_two_numbers_and_divide (number_1, number_2):
        if number_1 <=0 or number_2 <=0:
            return "Please choose a number higher than 0"
        else: 
            sum_of_addition = number_1 + number_2
            half_of_sum = sum_of_addition / 2 
            return half_of_sum




number_1 = 100 
number_2 = 400 

result = add_two_numbers_and_divide(number_1,number_2) 
print (result)  