import math

#Breif instructions to user
print("This program helps you find the lenght of adjacent and opposite sides of a right angled triangle by providing an angle and the lenght of the hypothenus")


#checking the value of angle to make sure it is a number less than or equal to 45 and more than 0
min_angle_value = 0.0
max_angle_value = 45.0
def get_Angle(prompt, min_angle_value , max_angle_value):
    while True:
        try:
            Angle = float(input(prompt))
            if min_angle_value  < Angle <= max_angle_value:
                return Angle
            else:
                print(f"Please enter a value greater than {min_angle_value } but less than or equal to {max_angle_value}")
        except ValueError:
            print("Invalid input. Please enter a number.")

#getting angle value from user
Angle = get_Angle(f"Enter an angle greater than {min_angle_value } but less than or equal to {max_angle_value}: ", min_angle_value , max_angle_value)

#converting angle to radian
angle_radians = math.radians(Angle)


#checking the value of hypothenus provided to make sure it is a number more than 0(not a negative number)

def get_Hypo(prompt):
    while True:
        try:
            Hypothenus = float(input(prompt))
            if Hypothenus > 0:
                return Hypothenus
            else:
                print("please enter a value greater than 0")

        except ValueError: 
            print("Invalid input. Please enter a number.")

#getting hypothenus from user 
Hypothenus = get_Hypo("Enter hypothenus value grater than 0: ")




# finding the lentgh of adjacent side from user input
def findAdjacent():
    Adjacent = Hypothenus*math.cos(angle_radians)
    print(f"The length of the adjacent side is {Adjacent}m")
    
findAdjacent()

#finding the lenght of opposite side
def findOpposite():
    Opposite = Hypothenus*math.sin(angle_radians)
    print(f"The length of the opposite side is {Opposite}m")

findOpposite()