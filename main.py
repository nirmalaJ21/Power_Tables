print("$" *50)
print('Welcome to power table'.upper())
print("$" *50)
option = 'y'              #Variable to store user's choice to continue entering value for power table'
start = 1
user_Input = 0
val_list =[]
#While loop to control execution of program until the  user input is 'y'
while True:
    # While loop to control until user input  valid integer value grater than 0
    while True :
        # While loop to control until user input  valid  number
        while True:
            try:                  # try catch exception block to check valid data entry else throw error msg.(line 8 - 12)
                user_Input = int(input("\t \t\nPlease enter an integer"))
                break               # break out of the inner while loop if user provided number is integer
            except ValueError:
                 print("oops! That was not a valid integer.Please try again...")
                 continue          #Continue while loop if user didn't provide valid data
        if int(user_Input) <= 0 :  # checking condition for negative integer)
            print("\t\n Please enter a valid positive  number ")  # print valid message
            continue  # continue to  check for valid input >0
        else:
            break  # if number is >0  continue with rest of the code

    print("{:<10} {:<10} {:<10}".format('Number', 'Square', 'Cube'))    #print header of the power table  left-align each header within a column that is 10 characters wide.
    print("-" * 6,"\t", "-" * 6, "\t", "-" * 6)                         #print -- line(count of 6) under the header printed  in above print statement
    for num in range(start, user_Input+ 1):                             #for loop in the range from 0 to user provided value + 1 to calculate squre and cube
            square = num ** 2                                           # multiply num two times to give square
            cube = num ** 3                                             # multiply num 3 times to give cube
            print("{:<10} {:<10} {:<10}".format(num, square, cube))     #print values of num , sqaure and cube in each iteration of for loop

#Define the number of columns in the table
    num_cols = user_Input
# Define the width of each column in the table
    col_width = 4
    print("\t\n\nMultiplication Tables from 1 to {}".format(num_cols))
    print("\n")

    tableHeader = "    "       # Variable will display the table header 1,2,3...
    tableSubHeader = "    "  # variable will hold the sign = under each table header value

    for num in range(1, num_cols + 1):  # loop to create table header and sub header
        tableHeader = tableHeader + str(num).rjust(col_width)
        tableSubHeader = tableSubHeader + "=".rjust(col_width)
    print(tableHeader)
    print(tableSubHeader)

    for num in range(1, num_cols+1 ): # Iterate through each row of the table and format the values to create rest of the table
        row_vals = []
        for num1 in range (1,num_cols + 1):
         i = num * num1
         row_vals.append(str(i).rjust(col_width))
        print(str(num) + " " + "|",''.join(row_vals))  #Print Multiplication table, here .join is use to join all rows
    # End of multiplication logic
    option = input("\t\t \nWould you like to continue y/n")
    if option.lower() == 'y':
        print("Continue..")
    elif option.lower() == 'n':
        print("Exiting...")
        break                                                           #Break out of the main/outer while loop if user don't want to continue
    else:
        print("Invalid input, please enter 'y' or 'n'.")



