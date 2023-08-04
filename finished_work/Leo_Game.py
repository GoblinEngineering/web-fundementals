#A better way to have done it would have been to use a dictionary instead of an array but her goes.

 

# store the input and the value of input in a multidementioanl array

List = [ ["What is the price of a child's meal? ", 0.0],

["What is the price of an adult's meal? ",0.0],

["How many children are there? ",0.0],

["How many adults are there? ", 0.0],

["What is the sales tax rate? ", 0.0],

["What is the payment amount? ",0.0],

["Total",0.0]

]

 

#function to check if the input is a number

def is_number(value):

try:

    float(value)

    return 1

except:

    print("ERROR: Please enter a whole number or a decimal!")

    return 0

 

#payment function

def payment_amount(param):

#get the prayment_amount

inputValue = input(List[param][0])

 

#check if it is a number

if(is_number(inputValue)) == 1:

List[param][1] = float(inputValue)

 

#check if this value is >= to the total

if (List[param][1] >= List[6][1]):

change = List[param][1] - List[6][1]

print(f"Change: ${change:,.2f}")

 

else:

print("ERROR! Entered value must be >= the Total!")

payment_amount(param)

 

#repeat if ther was an error

else:

payment_amount(param)

 

 

#main function

def meal_price_calculator(param):

#get the input that is at [index][0]

inputValue = input(List[param][0])

 

input_type = is_number(inputValue)

 

#check if the input value is a number

if ( input_type) == 1:

#if value is accepted then save it using its index

List[param][1] = float(inputValue)

 

# then increment the index

param += 1

 

# check if we reached the 5th index which has the value 6, remember arrays are 0 indexed

if (param <= 4):

# call the function again to go to the next index

meal_price_calculator(param)

else:

child_total = List[0][1] * List[2][1]

adult_total = List[1][1] * List[3][1]

subtotal = child_total + adult_total

sales_tax = List[4][1]

total = subtotal + sales_tax

 

#create a new entry in the List array for the total

List[6][0] = "total"

List[6][1] = total

 

print("")

print(f"Subtotal: ${subtotal:,.2f}")

print(f"Sales Tax: ${sales_tax:,.2f}")

print(f"Total: ${total:,.2f}")

print("")

 

payment_amount(5)

 

 

#if the value was not accepted then the user would have been told in an error.

#now prompt them again to enter the correct value for the same input

else:

meal_price_calculator(param)

 

 

meal_price_calculator(0)

 

 

Sent from Mail for Windows

 