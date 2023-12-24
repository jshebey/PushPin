class Part:
    def __init__(self, part_number):
        self.part_number = part_number
        self.data = None
        self.manufacturer = None
        self.resistance = None
        self.capacitance = None
        self.tolerance = None
        self.voltage = None
        self.size = None
        self.power = None
        self.dielectric = None

    def find_res_data(self):
        if(self.part_number[0:5] == 'RK73H'):
            self.manufacturer = 'KOA (RK73H series)'
            self.data = []
        elif(self.part_number[0:3] == 'FRC'):
            self.manufacturer = 'Kamaya (FRC series)'
            self.data = []
        elif(self.part_number[0:2] == 'RR'):
            self.manufacturer = 'Susumu (RR series)'
            self.data = []
        elif(self.part_number[0:2] == 'RC'):
            self.manufacturer = 'YAGEO (RC_L series)'
            self.data = []
        elif(self.part_number[0:3] == 'CRM'):
            self.manufacturer = 'Bourns (CRM series)'
            self.data = []
        else:
            pass

    def find_cap_data(self):
        if(self.part_number[0] == 'C'):
            if(self.part_number[5] == 'X' or self.part_number[5] == 'N' or self.part_number[5] == 'C'):
                if((self.part_number[6]).isnumeric() and (self.part_number[7]).isnumeric() and (self.part_number[8]).isnumeric()):
                    self.manufacturer = 'KEMET (MLCC series)'
                    self.data = []
                else:
                    if((self.part_number[9]).isalpha()):
                        self.manufacturer = 'TDK (C series)'
                        self.data = []
                    else:
                        self.manufacturer = 'Dafron (MLCC series)'
                        self.data = []
        elif(self.part_number[0:2] == 'MA'):
            self.manufacturer = 'Meritek (MA series)'
            self.data = []
        elif(self.part_number[0:3] == 'KAM'):
            self.manufacturer = 'AVX (KAM series)'
            self.data = []
        else:
            pass

    def res_decode(self):
        pass

    def cap_decode(self):
        pass

    def display_info(self):
        # Add a method to display information about the part
        print(f"Part Number: {self.part_number}")
        # Print other decoded information