from part import Part
import pandas as pd
import openpyxl as pyxl

class Scrub:
    def __init__(self, bom_file):
        self.bom_file = bom_file
        #Dataframe made from the BOM file
        self.df = pd.read_excel(bom_file)
        #Output excel file
        self.partList = pyxl.Workbook()
        self.currSheet = self.partList.active
        self.partNumberCol = 'A'
        self.valueCol = 'B'
        self.sizeCol = 'C'
        self.toleranceCol = 'D'
        self.miscCol = 'E'
        self.voltageCol = 'F'
        self.rowCount = 1

    def process_bom(self):
        #Loops over every part in the BOM
        for index, row in self.df.iterrows():
            schematicLabel = row['Schematic']
            #Grabs the part name
            partName = row['Part Number']
            #Creates a part object
            part = Part(partName)
            #Determines if part is a resistor, capacitor, or neither
            if(schematicLabel[0] == 'R'):
                part.find_res_data()
                part.res_decode()
                #Outputs the decoded part values on the Excel sheet
                #part.display_info(index)
            elif(schematicLabel[0] == 'C'):
                part.find_cap_data()
                part.cap_decode()
                #Outputs the decoded part values on the Excel sheet
                #part.display_info(index)
            else:
                print("NOT PART")
            self.rowCount += 1
            self.add_part(part, schematicLabel)
        self.partList.close()
    
    def add_part(self, part, schematicLabel):
        self.currSheet[self.partNumberCol + str(self.rowCount)] = part.partNumber
        if(schematicLabel[0] == 'R'):
            self.currSheet[self.valueCol + str(self.rowCount)] = part.resistance
            self.currSheet[self.miscCol + str(self.rowCount)] = part.power
        else:
            self.currSheet[self.valueCol + str(self.rowCount)] = part.capacitance
            self.currSheet[self.miscCol + str(self.rowCount)] = part.dielectric
        self.currSheet[self.sizeCol + str(self.rowCount)] = part.size
        self.currSheet[self.toleranceCol + str(self.rowCount)] = part.tolerance
        self.currSheet[self.voltageCol + str(self.rowCount)] = part.voltage
        self.partList.save('output.xlsx')