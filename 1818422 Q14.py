import math 

#checking if the sum of angles provided is less than 180
min_angle_value = 0.0
max_angle_value = 180.0
def get_Angle(prompt, min_angle_value , max_angle_value):
    while True:
        try:
            Angle = float(input(prompt))
            if min_angle_value  < Angle < max_angle_value:
                return Angle
            else:
                print(f"Please enter a value greater than {min_angle_value } but less than  {max_angle_value}")
        except ValueError:
            print("Invalid input. Please enter a number.")

#getting angles from user 
Alpha = get_Angle(f"Enter an angle(Alpha) greater than {min_angle_value } but less than  {max_angle_value}: ", min_angle_value , max_angle_value)
Gamma = get_Angle(f"Enter an angle greater(Gamma) than {min_angle_value } but less than  {max_angle_value}: ", min_angle_value , max_angle_value)



#checking the value of the length provided 
def get_A(prompt):
    while True:
        try:
            LengthA = float(input(prompt))
            if LengthA > 0:
                return LengthA
            else:
                print("please enter a value greater than 0")

        except ValueError: 
            print("Invalid input. Please enter a number.")

#getting length A from user 
LengthA = get_A("Enter Length value grater than 0: ")

#calculating angle beta and the length of side B
def findB(Alpha, Gamma):
    Beta = 180-(Gamma+Alpha)
    print(f"The angle Beta is {Beta}")
    LengthB = (LengthA*math.sin(math.radians(Beta)))/math.sin(math.radians(Alpha))
    print(f"the length of the side B is {LengthB} m")
    

findB(Alpha,Gamma)