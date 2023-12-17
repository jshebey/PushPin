class Part:
    def __init__(self, part_number):
        self.part_number = part_number
        self.manufactuer = None
        self.resistance = None
        self.capacitance = None
        self.tolerance = None
        self.voltage = None
        self.size = None

    def decode(self):
        self.find_manufacturer()
        self.find_resistance()
        self.find_capacitance()
        self.find_tolerance()
        self.find_voltage()
        self.find_size()
    
    def find_manufacturer(self):
        pass
    
    def find_resistance(self):
        pass
    
    def find_capacitance(self):
        pass

    def find_tolerance(self):
        pass
    
    def find_voltage(self):
        pass
    
    def find_size(self):
        pass

    def display_info(self):
        # Add a method to display information about the part
        print(f"Part Number: {self.part_number}")
        # Print other decoded information