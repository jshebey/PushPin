from tables import *

class Part:
    def __init__(self, part_number):
        self.partNumber = part_number
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
        #Determines which resistor family the part falls under
        if(self.partNumber[0:5] == 'RK73H'):
            self.manufacturer = 'KOA (RK73H series)'
            #[size string, size table, convert, tolerance string, tolerance table, convert, power string, power table, convert, voltage string, voltage table, convert, resistance string]
            self.data = [
                self.partNumber[5:7], koaSizeTable, 1,          #size data 
                self.partNumber[15],  koaToleranceTable, 1,     #tolerance data
                self.partNumber[5:7], koaPowerTable, 1,         #power data
                self.partNumber[5:7], koaVoltageTable, 1,       #voltage data
                self.partNumber[11:15]                          #resistance
            ]

        elif(self.partNumber[0:3] == 'FRC'):
            self.manufacturer = 'Kamaya (FRC series)'
            self.data = [
                self.partNumber[3:5], kamayaSizeTable, 1,          #size data 
                self.partNumber[11],  kamayaToleranceTable, 1,     #tolerance data
                self.partNumber[3:5], kamayaPowerTable, 1,         #power data
                self.partNumber[3:5], kamayaVoltageTable, 1,       #voltage data
                self.partNumber[8:11]                              #resistance
            ]

        elif(self.partNumber[0:2] == 'RR'):
            self.manufacturer = 'Susumu (RR series)'
            self.data = [
                self.partNumber[2:6], susumuSizeTable, 1,          #size data 
                self.partNumber[12],  susumuToleranceTable, 1,     #tolerance data
                self.partNumber[2:6], susumuPowerTable, 1,         #power data
                self.partNumber[2:6], susumuVoltageTable, 1,       #voltage data
                self.partNumber[8:11]                              #resistance
            ]

        elif(self.partNumber[0:2] == 'RC'):
            self.manufacturer = 'YAGEO (RC_L series)'
            self.data = [
                self.partNumber[2:6], 'N/A', 0,                    #size data 
                self.partNumber[6],  yageoToleranceTable, 1,       #tolerance data
                self.partNumber[2:6], yageoPowerTable, 1,          #power data
                self.partNumber[2:6], yageoVoltageTable, 1,        #voltage data
                self.partNumber[11:15]                             #resistance
            ]

        elif(self.partNumber[0:3] == 'CRM'):
            self.manufacturer = 'Bourns (CRM series)'
            self.data = [
                self.partNumber[3:7], 'N/A', 0,                    #size data 
                self.partNumber[8],  bournsToleranceTable, 1,      #tolerance data
                self.partNumber[3:7], bournsPowerTable, 1,         #power data
                self.partNumber[3:7], bournsVoltageTable, 1,       #voltage data
                self.partNumber[11:15]                             #resistance
            ]

        else:
            pass

    def find_cap_data(self):
        #Determines which capacitor family the part falls under
        if(self.partNumber[0] == 'C'):
            if(self.partNumber[5] == 'X' or self.partNumber[5] == 'N' or self.partNumber[5] == 'C'):
                if((self.partNumber[6]).isnumeric() and (self.partNumber[7]).isnumeric() and (self.partNumber[8]).isnumeric()):
                    self.manufacturer = 'KEMET (MLCC series)'
                    self.data = [
                        self.partNumber[1:5], 'N/A', 0,                    #size data 
                        self.partNumber[9],  kemetToleranceTable, 1,       #tolerance data
                        self.partNumber[11], kemetDielectricTable, 1,      #dielectric data
                        self.partNumber[10], kemetVoltageTable, 1,        #voltage data
                        self.partNumber[6:9]                               #capactiance
                    ]

                else:
                    if((self.partNumber[9]).isalpha()):
                        self.manufacturer = 'TDK (C series)'
                        self.data = [
                            self.partNumber[1:5], 'N/A', 0,                    #size data 
                            self.partNumber[13], tdkToleranceTable, 1,         #tolerance data
                            self.partNumber[5:8], 'N/A', 0,                    #dielectric data
                            self.partNumber[8:10], tdkVoltageTable, 1,         #voltage data
                            self.partNumber[10:13]                             #capactiance
                        ]

                    else:
                        self.manufacturer = 'Dafron (MLCC series)'
                        self.data = [
                            self.partNumber[1:5], darfonSizeTable, 1,          #size data 
                            self.partNumber[11], darfonToleranceTable, 1,      #tolerance data
                            self.partNumber[5:8], 'N/A', 0,                    #dielectric data
                            self.partNumber[12], darfonVoltageTable, 1,        #voltage data
                            self.partNumber[8:11]                              #capactiance
                        ]

        elif(self.partNumber[0:2] == 'MA'):
            self.manufacturer = 'Meritek (MA series)'
            self.data = [
                self.partNumber[2:6], 'N/A', 0,                    #size data 
                self.partNumber[11], meritekToleranceTable, 1,     #tolerance data
                self.partNumber[6:8], meritekDielectricTable, 1,   #dielectric data
                self.partNumber[12:15], 'N/A', 0,                  #voltage data
                self.partNumber[8:11]                              #capactiance
            ]

        elif(self.partNumber[0:3] == 'KAM'):
            self.manufacturer = 'AVX (KAM series)'
            self.data = [
                self.partNumber[3:5], avxSizeTable, 1,             #size data 
                self.partNumber[13], avxToleranceTable, 1,         #tolerance data
                self.partNumber[6:8], avxDielectricTable, 1,       #dielectric data
                self.partNumber[8:10], avxVoltageTable, 1,         #voltage data
                self.partNumber[10:13]                             #capactiance
            ]

        else:
            pass

    def res_decode(self):
        #Checks if the size code needs to be converted
        if(self.data[2]):
            #Searches size table
            self.size = next((item[1] for item in self.data[1] if item[0] == self.data[0]), 'UNKNOWN')
        else:
            self.size = self.data[0]   
        
        #Checks if the tolerance code needs to be converted
        if(self.data[5]):
            #Searches tolerance table
            self.tolerance = next((item[1] for item in self.data[4] if item[0] == self.data[3]), 'UNKNOWN') 
        else:
            self.tolerance = self.data[3]  
        
        #Checks if the power code needs to be converted
        if(self.data[8]):
            #Searches power table
            self.power = next((item[1] for item in self.data[7] if item[0] == self.data[6]), 'UNKNOWN') 
        else:
            self.power = self.data[6]

        #Checks if the voltage code needs to be converted
        if(self.data[11]):
            #Searches voltage table
            self.voltage = next((item[1] for item in self.data[10] if item[0] == self.data[9]), 'UNKNOWN') 
        else:
            self.voltage = self.data[9]   

        print('Part Number: ' + self.partNumber + ', Size: ' + self.size + ', Tolerance: ' + self.tolerance + ', Power: ' + self.power + ', Voltage: ' + self.voltage) 


    def cap_decode(self):
        #Checks if the size code needs to be converted
        if(self.data[2]):
            #Searches size table
            self.size = next((item[1] for item in self.data[1] if item[0] == self.data[0]), 'UNKNOWN')
        else:
            self.size = self.data[0]   
        
        #Checks if the tolerance code needs to be converted
        if(self.data[5]):
            #Searches tolerance table
            self.tolerance = next((item[1] for item in self.data[4] if item[0] == self.data[3]), 'UNKNOWN') 
        else:
            self.tolerance = self.data[3]  
        
        #Checks if the dielectric code needs to be converted
        if(self.data[8]):
            #Searches dielectric table
            self.dielectric = next((item[1] for item in self.data[7] if item[0] == self.data[6]), 'UNKNOWN') 
        else:
            self.dielectric = self.data[6]

        #Checks if the voltage code needs to be converted
        if(self.data[11]):
            #Searches voltage table
            self.voltage = next((item[1] for item in self.data[10] if item[0] == self.data[9]), 'UNKNOWN') 
        else:
            self.voltage = self.data[9]   

        print('Part Number: ' + self.partNumber + ', Size: ' + self.size + ', Tolerance: ' + self.tolerance + ', Dielectric: ' + self.dielectric + ', Voltage: ' + self.voltage) 

    def display_info(self):
        # Add a method to display information about the part
        print(f"Part Number: {self.partNumber}")
        # Print other decoded information