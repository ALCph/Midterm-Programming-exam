# 1.)
# A problem involving grade reading and sorting

# Opening the txt and storing the lines
with open('grades.txt', 'r') as file:
    lines = file.readlines()
    
# Some blank variables for use later
grades = []
total_students = 0
above_average = 0

# A loop to split the names and grades apart and append the blank list and total_students variable
for i in lines:
    list_with_both = i.split()
    grade = float(list_with_both[1])
    grades.append(grade)
    total_students += 1
    
# Calculations
total_grade_count = sum(grades)
average_grade = total_grade_count / total_students

# A loop to get above average grades using the newly appended grades list
for i in grades:
    if i > average_grade:
        above_average += 1

# Writing the output to a new file
# When I first tested this I forgot the \n and the results text looked funky, I still dont have the hang of using those
with open('results.txt', 'w') as results_file:
    results_file.write(f"Average class grade: {average_grade:.2f}\n")
    results_file.write(f"Number of students in class that scored above the average: {above_average}\n")
#-----------------------------------------------------------


# 2.)
# A problem about making new lists using integers from an existing list

import random
# Originally I was going to create a list with sample numbers in it, but thought that generating a random list might be fun

# A for loop to create a random list of numbers and add them to a list. I settled on 5 random numbers to make this easier to read
og_list = [random.randint(1, 101) for i in range(5)]  

# The function
def transform_data(list):
    # A for loop to create new list containing each integer squared
    list_squared = [num ** 2 for num in list]
    
    # Calculate the sum of the squared values
    sum_of_squares = sum(list_squared)
    
    #Printing the output
    print("Original list:", og_list)
    print("Squared list:", list_squared)
    print("Sum of Squared list:", sum_of_squares)
    
    # A return statement for posterity. This is only useful if the function was longer and needed to call on the variables right(?)
    return list_squared, sum_of_squares
    
# Calling the function using the random list
transform_data(og_list)
