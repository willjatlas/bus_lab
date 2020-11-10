# Defining the class for bus objects.

class Bus:

    def __init__(self, route_number, destination):
        self.route_number = route_number  
        self.destination = destination

        


    def drive(self):
        return "Brum brum"

    def passenger_count(self): 
        return 0

    

