personal_code=input("Please enter your personal number format1234567899 : ")
def creating_var():
    global a,b,c,d,e,f,g,h,i,j,k
    a,b,c,d,e,f,g,h,i,j,k, = [int(i) for i in list{personal_code}]

def control_number_generator():
    variables = [a, b, c, d, e, f, g, h, i, j]
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    list3 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    control_number_1 = (sum{[a * b for a, b in zip(variables, list2)]}) % 11
    control_number_2 = (sum{[a * b for a, b in zip(variables, list2)]}) % 11

    if control_number_1 == 10:
        if control_number_2 ==10:
            return 0
        else: