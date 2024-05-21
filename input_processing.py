# input_processing.py
# DESTIN SABA, ENSF 692 P24

# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.

class Sensor:

    def __init__(self):
        # Initialize the sensor status with default values
        self.traffic_light = "green"
        self.pedestrian_status = "no"
        self.vehicle_status = "no"

    # update_status() acts on the Sensor class. 
    # It calls the get_input() function to ask the user for input for the traffic light, pedestrian, and vehicle status.
    # It then processes the input, updates the Class instance variables and prints the result by calling the print_message() function.
    def update_status(self): 
        choice = 1
        while(choice != 0):
            # Get user input for the detected changes
            choice, change = get_input()
            if (choice == 1): 
                # Update traffic light status and print updated status message
                self.traffic_light = change
                print_message(self)
            elif (choice == 2):
                # Update pedestrian status and print updated status message
                self.pedestrian_status = change
                print_message(self)
            elif (choice == 3):
                # Update vehicle status and print updated status message
                self.vehicle_status = change
                print_message(self)
            elif (choice ==4):
                # Print status message without any changes
                print_message(self)

# The print_message() function accepts a sensor object to print the action message and current status.
# Any scenario where a red light, a pedestrian or a vehicle are detected will display the message "STOP"
# A green light with no pedestrian or vehicle detected will display the message "Proceed"
# A yellow light with no pedestrian or vehicle detected will display the message "Caution"
# After the action message, the current status of each monitored condition will be printed

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

# get_input() creates the user interface that asks the user to input the detected status change
# If menu option 1, 2 or 3 are detected, the user will be prompted to specify the detected change:
#  * A traffic light can be "green", "yellow", or "red"
#  * Pedestrian status can be "yes" or "no"
#  * Vehicle status can be "yes" or "no"

def get_input():

    while (True):
        print("Are changes detected in the vision input?")
        try:
            # Ask user to select an option for input detection
            choice = int(input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: "))
        except ValueError:
            # Handle invalid input
            print("You must select either 1, 2, 3, or 0.")
            print("")
            return 5,0

        if choice == 0:
            # End the program
            return 0,0
        elif (choice == 1):
            # Ask for traffic light change
            change = input("What change has been identified?: ")
            if ((change == "green") or (change == "yellow") or (change == "red")):
                return choice, change
            else:
                # Handle invalid input
                print("Invalid vision change.")
                return 4,0

        elif (choice == 2):
            # Ask for pedestrian status change
            change = input("What change has been identified?: ")
            if ((change == "yes") or (change == "no")):
                return choice, change
            else:
                # Handle invalid input
                print("Invalid vision change.")
                return 4,0

        elif (choice == 3):
            # Ask for vehicle status change
            change = input("What change has been identified?: ")
            if ((change == "yes") or (change == "no")):
                return choice, change
            else:
                # Handle invalid input
                print("Invalid vision change.")
                return 4,0
                
        else:
            # Handle invalid menu choice
            print("You must select either 1, 2, 3, or 0.")
            print("")

# Creates a Sensor object and runs the update_status() function.
def main():
    # Initialize a Sensor object
    status = Sensor()
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    # Start the status update process
    status.update_status()
    exit()

if __name__ == '__main__':
    main()

