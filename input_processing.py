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
    def update_status(self, light, ped, vehicle): # You may decide how to implement the arguments for this function
        self.traffic_light = light
        self.pedestrian_status = ped
        self.vehicle_status = vehicle



# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    if ((sensor.traffic_light == "red") or (sensor.pedestrian_status == "yes") or (sensor.vehicle_status == "yes")):
        print("STOP")
    elif ((sensor.traffic_light == "green") and (sensor.pedestrian_status == "no") and (sensor.vehicle_status == "no")):
        print("Proceed")
    else:
        print("Caution")

    print("")
    print("Light = " + sensor.traffic_light + " , Pedestrian = " + sensor.pedestrian_status + " , Vehicle = " + sensor.vehicle_status + " .")
    print("")




# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    
    light = Sensor()
    light.update_status("red","yes","yes")
    print_message(light)





# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

