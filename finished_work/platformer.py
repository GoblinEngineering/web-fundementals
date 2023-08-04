
# land=[
# "         x",
# "         x",
# "         x",
# "         x",
# "  xxxx   x",
# "         x",
# "         x",
# "    x    x",
# "    x    x",
# "xxxxxxxxxx"
# ]




# land=[
#     "x","x","x","x","x","x","x","x",
#     "x"," "," "," "," "," "," ","x",
#     "x"," "," "," "," "," "," ","x",
#     "x"," "," "," "," "," "," ","x",
#     "x"," "," "," "," "," "," ","x",
#     "x"," "," "," "," "," "," ","x",
#     "x"," "," "," "," "," "," ","x",
#     "x"," "," "," "," "," "," ","x",
#     "x"," "," "," "," "," "," ","x",
#     "x"," "," "," "," "," "," ","x",
#     "x"," "," "," "," "," "," ","x",
#     "x"," "," "," "," "," "," ","x",
#     "x"," "," "," "," "," "," ","x",
#     "x"," "," "," "," "," "," ","x",
#     "x","x","x","x","x","x","x","x",
# ]
# for block in land:
#     print (block)

# a = "the"
# b = "word"
# print(a+" "+b) 

# a= a+b 
# print(a)
# a = " "
# if a == "x":
#     print("correct")
# else:
#     print("incorrect")
# for i in land:
#     print(i)


# print (land[1][0])
# row = 1
# collum=0
# print (land[row][collum])

# line = " "
# row = 0
# for b in land:
#     line = " "
#     for i in land[row]:
#        line= line+i
#     row = row + 1
#     print(line)


# if land[1][0] == " ":
#        print ("correct")
# else:
#         print("nah")




land =[
    ["x","x","x","x","x","x","x","x","x"],
    ["x"," "," "," "," "," "," "," ","x"],
    ["x"," "," "," "," "," "," "," ","x"],
    ["x"," ","x","x","x","x"," "," ","x"],
    ["x"," ","x"," "," "," ","x"," ","x"],
    ["x"," ","x"," "," "," ","x"," ","x"],
    ["x"," ","x"," "," "," ","x"," ","x"],
    ["x"," ","x","x","x","x"," "," ","x"],
    ["x"," ","x"," "," "," ","x"," ","x"],
    ["x"," ","x"," "," "," ","x"," ","x"],
    ["x"," ","x"," "," "," ","x"," ","x"],
    ["x"," ","x"," "," "," ","x"," ","x"],
    ["x"," ","x","x","x","x"," "," ","x"],
    ["x"," "," "," "," "," "," "," ","x"],
    ["x","x","x","x","x","x","x","x","x"]
]

line = " "
row = 0
for realrow in land:
    
    A= " "
    B= " "
    C= " "
    D= " "
    E= " "
    for i in land[row]:

        if i == "x":
            A = A + "XXXXXXXXXX" 
            B = B + "X        X" 
            C = C + "X        X"
            D = D + "X        X" 
            E = E + "XXXXXXXXXX"

        else:
            A += "          " 
            B += "          " 
            C += "          "
            D += "          " 
            E += "          "

    print(A)
    print(B)
    print(C)
    print(D)
    print(E) 
    row += 1
    
