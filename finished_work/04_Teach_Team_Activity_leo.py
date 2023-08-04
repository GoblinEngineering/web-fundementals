import math

# store the input and the value of input in a nested dictionary
formula_inputs_and_values = {
    "input_1" : {
        "name":"Mass",
        "input":"Mass (in kg): ",
        "value": 0
    },
    "input_2" : {
        "name":"Gravity",
        "input":"Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): ",
        "possible_values": {
            "earth": 9.8,
            "Jupiter": 24
        },
        "value": 0
    },
    "input_3": {
        "name": "Time",
        "input": "Time (in seconds): ",
        "value":0
    },
    "input_4": {
        "name":"Density",
        "input":"Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): ",
        "possible_values": {
            "air": 1.3,
            "Water": 1000
        },
        "value": 0
    },
    "input_5": {
        "name":"Cross Section",
        "input": "Cross sectional area (in m^2): ",
        "value": 0,
    },
    "input_6": {
        "name":"Drag Constant",
        "input": "Drag constant (0.5 for sphere, 1.1 for cylinder): ",
        "possible_values": {
            "sphere": 0.5,
            "cylinder": 1.1
        },
    }
}

#helper functions to check the inputs
#---check if input is number or decimal
def is_number(value):
    try:
        float(value)
        return True
    except:
        print("ERROR: Please enter a whole number or a decimal!")
        return False

#--check against "possible_values" element
def check_possible_values(key_name, dictionary_elements, value_to_find):
    #return this dictionary if we did not get a match
    value_to_return = {
        "pass_check": False,
        "message": f"ERROR: {value_to_find} does not match a predefined value for {key_name}!",
        "key": "unfound"
    }
    
    #get all the key/value pairs of the dictionary_elements
    list_of_items = dictionary_elements.items()
    
    #loop the items
    for item  in list_of_items:
        #check if the value from the item is = to the value_to_find
        if item[1] == value_to_find:
            # update the value_to_return dictionary
            value_to_return.update({"pass_check": True, "message":"Value was found", "key": item[0]})
            #end the loop
            break
        
    return value_to_return

# show the output 
def show_calculation_output():
    m = formula_inputs_and_values["input_1"]["value"]
    g = formula_inputs_and_values["input_2"]["value"]
    t = formula_inputs_and_values["input_3"]["value"]
    p = formula_inputs_and_values["input_4"]["value"]
    A = formula_inputs_and_values["input_5"]["value"]
    C = formula_inputs_and_values["input_6"]["value"]

    # First calculate c = 1/2 p A C
    c = (1 / 2) * p * A * C

    # Now calculate the velocity v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)*t))
    v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))

    print() # display a blank line
    print(f"The inner value of c is: {c:.3f}")
    print(f"The velocity after {t} seconds is: {v:.3f} m/s\n")

# continue working on the calculation
def continue_calculation(param, input_value):
    #if value is accepted then save it using the dictionary element value property
    formula_inputs_and_values[f"input_{param}"]["value"] = float(input_value)

    # then increment the param
    param += 1

    # check if we should continue the recursive loop
    if param <= len(formula_inputs_and_values):
        falling_object_speed_calculator(param)
    else:                         
        show_calculation_output()
    
#main function
print("\nWelcome to the velocity calculator. Please enter the following:\n")
def falling_object_speed_calculator(param):
    #get the input that is at formula_inputs_and_values["input_"+param]["input"]
    input_value = input(formula_inputs_and_values[f"input_{param}"]["input"])
    
    input_value_type_is_number = is_number(input_value)

    #check if the input value is a number
    if ( input_value_type_is_number) == True: 

        # now check if the "possible values" key exist in formula_inputs_and_values["input_"+param]
        if "possible_values" in formula_inputs_and_values[f"input_{param}"]:

            # check if the value entered matched a "possible_value" value
            possible_value_check = check_possible_values(formula_inputs_and_values[f"input_{param}"]["name"], formula_inputs_and_values[f"input_{param}"]["possible_values"], float(input_value))

            if possible_value_check["pass_check"]:
                continue_calculation(param, input_value)
            else:
                # show error message and prompt again with the same input
                print(possible_value_check["message"])
                falling_object_speed_calculator(param)

        else:
            continue_calculation(param, input_value)
    
            
    #if the value was not accepted then the user would have been told in an error message. 
    #now prompt the user again to enter the correct value for the same input
    else:
        falling_object_speed_calculator(param)

        
falling_object_speed_calculator(1)