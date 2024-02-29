#Task 1
def temperature_converter(cel):
    temp_f = cel * 9/5 + 32
    temp_k = cel + 273.15
    print("The temperature in Farenheits is {}.The temperature in Kelvins is {} ".format(temp_f, temp_k))

temperature_converter(25)

#Task 2
def temp_and_vol(t1,v1,t2,v2):
    volume = v1 + v2
    temp = (v1 * t1 + v2 * t2) / volume
    print("The temperature of the mixture is {} and the volume is {}.".format(temp, volume))

temp_and_vol(30,50,50,70)

#Task 3
def calc():
    num_1 = int(input('Enter number_1'))
    num_2 = int(input('Enter number_2'))
    operation = input('Enter operation: "+","-","/","*"')
    if operation == "+":
        print(num_1+num_2)
    elif operation == "-":
        print(num_1-num_2)
    elif operation == "/":
        print(num_1/num_2)
    elif operation == "*":
        print(num_1*num_2)

calc()










