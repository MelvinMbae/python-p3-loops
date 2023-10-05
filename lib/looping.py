#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        # if i == 1:
        i -= 1

    print('Happy New Year!')

my_output = happy_new_year()
my_output

def square_integers(int_list):
  
    # Use list comprehensions

    # Any VariableName = what we want to do: define loop (for data in our variable)
    int_list = [pow(nums, 2) for nums in int_list]
    
    # or
    # int_list = [nums * nums for nums in int_list]

    return int_list


print(square_integers([1, 2, 3, 4, 5]))

def fizzbuzz():
    i = 1
    while i <= 100:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1
        

fizzbuzz()