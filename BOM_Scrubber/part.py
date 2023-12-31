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
        self.quantity = 0

    def find_res_data(self):
        #Determines which resistor family the part falls under
        if(self.partNumber[0:5] == 'RK73H'):
            self.koa_RK73H()

        elif(self.partNumber[0:3] == 'FRC'):
            self.kamaya_FRC()

        elif(self.partNumber[0:2] == 'RR'):
            self.susumu_RR()

        elif(self.partNumber[0:2] == 'RC'):
            self.yageo_RC_L()

        elif(self.partNumber[0:3] == 'CRM'):
            self.bourns_CRM()

        else:
            pass
    
    def koa_RK73H(self):
        self.manufacturer = 'KOA (RK73H series)'
        #[size string, size table, convert, tolerance string, tolerance table, convert, power string, power table, convert, voltage string, voltage table, convert, resistance string]
        self.data = [
            self.partNumber[5:7], koaSizeTable, 1,          #size data 
            self.partNumber[15],  koaToleranceTable, 1,     #tolerance data
            self.partNumber[5:7], koaPowerTable, 1,         #power data
            self.partNumber[5:7], koaVoltageTable, 1,       #voltage data
            self.partNumber[11:15], 0                       #resistance
            ]
    
    def kamaya_FRC(self):
        self.manufacturer = 'Kamaya (FRC series)'
        self.data = [
            self.partNumber[3:5], kamayaSizeTable, 1,          #size data 
            self.partNumber[11],  kamayaToleranceTable, 1,     #tolerance data
            self.partNumber[3:5], kamayaPowerTable, 1,         #power data
            self.partNumber[3:5], kamayaVoltageTable, 1,       #voltage data
            self.partNumber[8:11], 0                           #resistance
        ]

    def susumu_RR(self):
        self.manufacturer = 'Susumu (RR series)'
        end = len(self.partNumber) - 2
        self.data = [
            self.partNumber[2:6], susumuSizeTable, 1,          #size data 
            self.partNumber[12],  susumuToleranceTable, 1,     #tolerance data
            self.partNumber[2:6], susumuPowerTable, 1,         #power data
            self.partNumber[2:6], susumuVoltageTable, 1,       #voltage data
            self.partNumber[8:end], 0                           #resistance
        ]
    
    def yageo_RC_L(self):
        self.manufacturer = 'YAGEO (RC_L series)'
        end = len(self.partNumber) - 1
        self.data = [
            self.partNumber[2:6], 'N/A', 0,                    #size data 
            self.partNumber[6],  yageoToleranceTable, 1,       #tolerance data
            self.partNumber[2:6], yageoPowerTable, 1,          #power data
            self.partNumber[2:6], yageoVoltageTable, 1,        #voltage data
            self.partNumber[11:end], 1                          #resistance
        ]
    
    def bourns_CRM(self):
        self.manufacturer = 'Bourns (CRM series)'
        end = len(self.partNumber) - 3
        self.data = [
            self.partNumber[3:7], 'N/A', 0,                    #size data 
            self.partNumber[8],  bournsToleranceTable, 1,      #tolerance data
            self.partNumber[3:7], bournsPowerTable, 1,         #power data
            self.partNumber[3:7], bournsVoltageTable, 1,       #voltage data
            self.partNumber[11:end], 0                         #resistance
        ]

    def find_cap_data(self):
        #Determines which capacitor family the part falls under
        if(self.partNumber[0] == 'C'):
            if(self.partNumber[5] == 'X' or self.partNumber[5] == 'N' or self.partNumber[5] == 'C'):
                if((self.partNumber[6]).isnumeric() and (self.partNumber[7]).isnumeric() and (self.partNumber[8]).isnumeric()):
                    self.kemet_MLCC()
                else:
                    if((self.partNumber[9]).isalpha()):
                        self.tdk_c()
                    else:
                        self.dafron_MLCC()

        elif(self.partNumber[0:2] == 'MA'):
            self.meritek_MA()

        elif(self.partNumber[0:3] == 'KAM'):
            self.avx_KAM()

        else:
            pass
    
    def kemet_MLCC(self):
        self.manufacturer = 'KEMET (MLCC series)'
        self.data = [
            self.partNumber[1:5], 'N/A', 0,                    #size data 
            self.partNumber[9],  kemetToleranceTable, 1,       #tolerance data
            self.partNumber[11], kemetDielectricTable, 1,      #dielectric data
            self.partNumber[10], kemetVoltageTable, 1,         #voltage data
            self.partNumber[6:9]                               #capactiance
        ]
    
    def tdk_c(self):
        self.manufacturer = 'TDK (C series)'
        self.data = [
            self.partNumber[1:5], 'N/A', 0,                    #size data 
            self.partNumber[13], tdkToleranceTable, 1,         #tolerance data
            self.partNumber[5:8], 'N/A', 0,                    #dielectric data
            self.partNumber[8:10], tdkVoltageTable, 1,         #voltage data
            self.partNumber[10:13]                             #capactiance
        ]
    
    def dafron_MLCC(self):
        self.manufacturer = 'Dafron (MLCC series)'
        self.data = [
            self.partNumber[1:5], darfonSizeTable, 1,          #size data 
            self.partNumber[11], darfonToleranceTable, 1,      #tolerance data
            self.partNumber[5:8], 'N/A', 0,                    #dielectric data
            self.partNumber[12], darfonVoltageTable, 1,        #voltage data
            self.partNumber[8:11]                              #capactiance
        ]
    
    def meritek_MA(self):
        self.manufacturer = 'Meritek (MA series)'
        self.data = [
            self.partNumber[2:6], 'N/A', 0,                    #size data 
            self.partNumber[11], meritekToleranceTable, 1,     #tolerance data
            self.partNumber[6:8], meritekDielectricTable, 1,   #dielectric data
            self.partNumber[12:15], 'N/A', 0,                  #voltage data
            self.partNumber[8:11]                              #capactiance
        ]
    
    def avx_KAM(self):
        self.manufacturer = 'AVX (KAM series)'
        self.data = [
            self.partNumber[3:5], avxSizeTable, 1,             #size data 
            self.partNumber[13], avxToleranceTable, 1,         #tolerance data
            self.partNumber[6:8], avxDielectricTable, 1,       #dielectric data
            self.partNumber[8:10], avxVoltageTable, 1,         #voltage data
            self.partNumber[10:13]                             #capactiance
        ]


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

        #Logic for determining resistance
        #When resistance code is 3, or 4 digits, and can have R (for decimals) and last digit is multiplier
        if(self.data[13] == 0):
            resistance = self.data[12]
            #If resistance is 3 characters long, add a leading zero
            if(len(resistance) == 3):
                resistance = '0' + resistance
            #Multiplies the resistance by 10^-3 if there are three deciamals (.xxx)
            if(resistance[0] == 'R'):
                self.resistance = int(resistance[1:4]) * (10 ** -3)
                self.resistance = str(self.resistance) + ' ohms'
            #Multiplies the resistance by 10^-2 if there are two deciamals (x.xx)
            elif(resistance[1] == 'R'):
                self.resistance = int(resistance[0]) + (int(resistance[2:4]) * 0.01)
                self.resistance = str(self.resistance) + ' ohms'
            #Multiplies the resistance by 10^-1 if there is one deciamal (xx.x)
            elif(resistance[2] == 'R'):
                self.resistance = int(resistance[0:2]) + (int(resistance[3]) * 0.1)
                self.resistance = str(self.resistance) + ' ohms'
            #Converts R to a decimal (xxx.)
            elif(resistance[3] == 'R'):
                self.resistance = int(resistance[0:3])
                self.resistance = str(self.resistance) + ' ohms'
            #When there isn't a deciamal, the value is multiplied by 10^4th digit
            else:
                self.resistance = int(resistance[0:3]) * (10 ** int(resistance[3]))
                #Converts resistance to millions if it is bigger than 10^6
                if(int(resistance[3]) >= 6):
                    self.resistance = str(round(self.resistance * (10 ** -6), 2)) + ' M ohms'
                #Converts resistance to thousands if it is bigger than 10^3
                elif(int(resistance[3]) >= 3):
                    self.resistance = str(round((self.resistance * (10 ** -3)), 2)) + ' K ohms'
                #Otherwise it keeps the resistance in ohms
                else:
                    self.resistance = str(self.resistance) + ' ohms'

        #When resistance code is 2, 3, or 4 digits, and can have R (for decimals), K (for thousands), and M (for millions)
        elif(self.data[13] == 1):
            resistance = self.data[12]
            #If the resistance is two characters, two leading zeros are added
            if(len(resistance) == 2):
                resistance = '00' + resistance
            #If the resistance is three characters, one leading zero is added
            if(len(resistance) == 3):
                resistance = '0' + resistance
            #Converts R in ([1] spot) to a decimal in the resistance code
            if(resistance[1] == 'R'):
                self.resistance = int(resistance[0]) + (int(resistance[2]) * 0.1) + (int(resistance[3]) * 0.01)
                self.resistance = str(self.resistance) + ' ohms'
            #Converts R in ([2] spot) to a decimal in the resistance code
            elif(resistance[2] == 'R'):
                self.resistance = int(resistance[0:2]) + (int(resistance[3]) * 0.1)
                self.resistance = str(self.resistance) + ' ohms'
            #Converts R in ([3] spot) to a decimal in the resistance code
            elif(resistance[3] == 'R'):
                self.resistance = int(resistance[0:3])
                self.resistance = str(self.resistance) + ' ohms'
            #Converts K in ([1] spot) and multiplies the resistance value by a thousand
            elif(resistance[1] == 'K'):
                self.resistance = int(resistance[0]) * 1000 + (int(resistance[2]) * 100) + (int(resistance[3]) * 10)
                self.resistance = str(round(self.resistance * (10 ** -3), 2)) + 'K ohms'
            #Converts K in ([2] spot) and multiplies the resistance value by a thousand
            elif(resistance[2] == 'K'):
                self.resistance = int(resistance[0:2]) * 1000 + (int(resistance[3]) * 100)
                self.resistance = str(round(self.resistance * (10 ** -3), 2)) + 'K ohms'
            #Converts K in ([3] spot) and multiplies the resistance value by a thousand
            elif(resistance[3] == 'K'):
                self.resistance = int(resistance[0:3]) * 1000
                self.resistance = str(round(self.resistance * (10 ** -3), 2)) + 'K ohms'
            #Converts M in ([1] spot) and multiplies the resistance value by a million
            elif(resistance[1] == 'M'):
                self.resistance = (int(resistance[0]) * 1000000) + (int(resistance[2]) * 100000) + (int(resistance[3]) * 10000)
                self.resistance = str(round(self.resistance * (10 ** -6), 2)) + 'M ohms'
            #Converts M in ([2] spot) and multiplies the resistance value by a million
            elif(resistance[2] == 'M'):
                self.resistance = int(resistance[0:2]) * 1000000 + (int(resistance[3]) * 100000)
                self.resistance = str(round(self.resistance * (10 ** -6), 2)) + 'M ohms'
            #Converts M in ([3] spot) and multiplies the resistance value by a million
            elif(resistance[3] == 'M'):
                self.resistance = int(resistance[0:3]) * 1000000
                self.resistance = str(round(self.resistance * (10 ** -6), 2)) + 'M ohms'
            #Keeps resistance the same if there is no R, K, or M
            else:
                self.resistance = int(resistance)
                self.resistance = str(self.resistance) + ' ohms'
        #Prints the part characteristics in the terminal for debugging
        print('Part Number: ' + self.partNumber + ', Resistance: ' + str(self.resistance) + ', Size: ' + self.size + ', Tolerance: ' + self.tolerance + ', Power: ' + self.power + ', Voltage: ' + self.voltage) 


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
            #If the part is a Mertitek (MA series) capacitor, the voltage needs to be decoded
            if(self.manufacturer == 'Meritek (MA series)'):
                voltage = self.data[9]
                self.voltage = str(int(voltage[0:2]) * 10 ** int(voltage[2])) + ' V'
            else:
                self.voltage = self.data[9] + ' V'
        
        #Logic for determining capacitance
        #When capacitance code is 3, or 4 digits, and can have R (for decimals) and last digit is multiplier
        capacitance = self.data[12]
        #Adds a leading zero if the capacitance code is 3 digits
        if(len(capacitance) == 3):
            capacitance = '0' + capacitance
        #Multiples the capacitance by 10^-3 if first digit is R
        if(capacitance[0] == 'R'):
            self.capacitance = int(capacitance[1:4]) * (10 ** -3)
            self.capacitance = str(self.capacitance) + ' pF'
        #Multiplies the capacitance by 10^-2 if the second digit is R
        elif(capacitance[1] == 'R'):
            self.capacitance = int(capacitance[0]) + (int(capacitance[2:4]) * 0.01)
            self.capacitance = str(self.capacitance) + ' pF'
        #Multiplies the capacitance by 10^-1 if the third digit is R
        elif(capacitance[2] == 'R'):
            self.capacitance = int(capacitance[0:2]) + (int(capacitance[3]) * 0.1)
            self.capacitance = str(self.capacitance) + ' pF'
        #Multiplies the capacitance by 1 if the fourth digit is R
        elif(capacitance[3] == 'R'):
            self.capacitance = int(capacitance[0:3])
            self.capacitance = str(self.capacitance) + ' pF'
        else:
            #If there is no R in the capacitance code, the number is multiplied by 10^4th digit
            self.capacitance = round(int(capacitance[0:3]) * (10 ** int(capacitance[3])), 2)
            if(int(capacitance[3]) > 6):
                self.capacitance = str(round(self.capacitance * (10 ** -6), 2)) + ' uF'
            else:
                self.capacitance = str(self.capacitance) + ' pF'
        #Prints the part characteristics in the terminal for debugging
        print('Part Number: ' + self.partNumber + ', Capacitance: ' + str(self.capacitance) + ', Size: ' + self.size + ', Tolerance: ' + self.tolerance + ', Dielectric: ' + self.dielectric + ', Voltage: ' + self.voltage) 
