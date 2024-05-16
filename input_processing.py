# input_processing.py
# DESTIN SABA, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.traffic_light = "green"
        self.pedestrian_status = "no"
        self.vehicle_status = "no"

    # Replace these comments with your function commenting
    def update_status(self): # You may decide how to implement the arguments for this function
        choice = 1
        while(choice != 0):
            choice, change = get_input()
            if (choice == 1): 
                self.traffic_light = change
                print_message(self)
            elif (choice == 2):
                self.pedestrian_status = change
                print_message(self)
            elif (choice == 3):
                self.vehicle_status = change
                print_message(self)
            elif (choice ==4):
                print_message(self)



# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    print("")
    if ((sensor.traffic_light == "red") or (sensor.pedestrian_status == "yes") or (sensor.vehicle_status == "yes")):
        print("STOP")
    elif ((sensor.traffic_light == "green") and (sensor.pedestrian_status == "no") and (sensor.vehicle_status == "no")):
        print("Proceed")
    else:
        print("Caution")

    print("")
    print("Light = " + sensor.traffic_light + " , Pedestrian = " + sensor.pedestrian_status + " , Vehicle = " + sensor.vehicle_status + " .")
    print("")

#    If menu option 1, 2 or 3 are detected, the user should then be prompted to specify the detected change
#    A traffic light can be "green", "yellow", or "red"
#    Pedestrian status can be "yes" or "no"
#    Vehicle status can be "yes" or "no"

def get_input():

    while (True):
        print("Are changes detected in the vision input?")
        try:
            choice = int(input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: "))
        except ValueError:
            print("You must select either 1, 2, 3, or 0.")
            print("")
            return 5,0

        if choice == 0:
            return 0,0
        elif (choice == 1):
            change = input("What change has been identified?: ")
            if ((change == "green") or (change == "yellow") or (change == "red")):
                return choice, change
            else:
                print("Invalid vision change.")
                return 4,0

        elif (choice == 2):
            change = input("What change has been identified?: ")
            if ((change == "yes") or (change == "no")):
                return choice, change
            else:
                print("Invalid vision change.")
                return 4,0

        elif (choice == 3):
            change = input("What change has been identified?: ")
            if ((change == "yes") or (change == "no")):
                return choice, change
            else:
                print("Invalid vision change.")
                return 4,0
                
        else:
            print("You must select either 1, 2, 3, or 0.")
            print("")





# Complete the main function below
def main():
    status = Sensor()
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    status.update_status()
    exit()

    





# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

