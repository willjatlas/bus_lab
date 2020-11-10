# Defining a class for bus stop objects, 

class BusStop:
    # Constructor 
    def __init__(self, name):
        self.name = name 
        self.queue = []


    # Method that returns the length of the bus stop queue.
    def queue_length(self):
        return len(self.queue)

    # Method that adds a person to the bus stop queue.
    def add_to_queue(self, person):
        self.queue.append(person)
    
    # Method that clears the bus stop queue. 
    def clear(self):
        self.queue.clear()