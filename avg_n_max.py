#Code to input a series of number and get the max and average values of the list.
print("Type in the number you would like to find the max and average of:")
user_input = input()  #Obtains user input

input_to_int = [int(i) for i in user_input.split()] #Splits the input by the delimiter space

sum_input = sum([i for i in input_to_int])
average = sum_input // len(input_to_int)
maximium = max([int(i) for i in input_to_int])

print("Your max value is:", maximium, "And your average is:", average)
