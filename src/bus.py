# Defining the class for bus objects.

class Bus:
    # Constructor
    def __init__(self, route_number, destination):
        self.route_number = route_number  
        self.destination = destination
        self.passengers = []

        

    # Method that emulates the driving action .
    def drive(self):
        return "Brum brum"

    # Method that counts the passengers on the bus object.
    def passenger_count(self): 
        return len(self.passengers)
    
    # Method that picks up a person object and adds them to the busses passengers list.
    def pick_up(self, person):
        self.passengers.append(person)
    
    #Method that drops off a specified passenger object.
    def drop_off(self, person):
        self.passengers.remove(person)

    # Driver has had enough, get off, everyone...
    def empty(self):
        self.passengers.clear()



    

