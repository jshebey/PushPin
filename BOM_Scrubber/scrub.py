from part import Part
import pandas as pd
import openpyxl as pyxl
import os

class Scrub:
    def __init__(self, bom_file, rowTotal):
        self.bom_file = bom_file
        #Dataframe made from the BOM file
        self.df = pd.read_excel(bom_file)
        #Output excel file, only creates a new Excel sheet if it doesn't already exist
        self.partList = pyxl.load_workbook('output.xlsx') if os.path.exists('output.xlsx') else pyxl.Workbook()
        self.currSheet = self.partList.active
        self.partNumberCol = 'A'
        self.manufacturerCol = 'B'
        self.valueCol = 'C'
        self.sizeCol = 'D'
        self.toleranceCol = 'E'
        self.miscCol = 'F'
        self.voltageCol = 'G'
        self.quantityCol = 'H'
        self.rowCount = rowTotal

    def process_bom(self):
        #Loops over every part in the BOM
        for index, row in self.df.iterrows():
            schematicLabel = row['Schematic']
            #Grabs the part name
            partName = row['Part Number']
            #Creates a part object
            part = Part(partName)
            #Quantity is grabbed from the quantity column on the BOM
            part.quantity = int(row['Quantity'])
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
            
            self.update_output(part, schematicLabel)

    def update_output(self, part, schematicLabel):
        #Flag for checking if the part is already listed in the output
        partExists = False
        #Loops through each row of the output Excel sheet
        for row in range(1, self.rowCount + 1):
            #if the part is already listed, update the quantity and set the flag true
            if((self.currSheet['A' + str(row)]).value == part.partNumber):
                self.currSheet['H' + str(row)] = int(self.currSheet['H' + str(row)].value) + part.quantity
                self.partList.save('output.xlsx')
                partExists = True
        #If the part is not already listed, create a new row in the output sheet    
        if(not partExists):
            self.rowCount += 1
            self.new_part(part, schematicLabel)
    
    def new_part(self, part, schematicLabel):
        #When a new part is listed, each value is placed in the respective cell
        self.currSheet[self.partNumberCol + str(self.rowCount)] = part.partNumber
        self.currSheet[self.manufacturerCol + str(self.rowCount)] = part.manufacturer
        #If the part is a resistor, the resistance and power characteristics are added
        if(schematicLabel[0] == 'R'):
            self.currSheet[self.valueCol + str(self.rowCount)] = part.resistance
            self.currSheet[self.miscCol + str(self.rowCount)] = part.power
        #If the part is a capacitor, the capacitance and dielectric characteristics are added
        else:
            self.currSheet[self.valueCol + str(self.rowCount)] = part.capacitance
            self.currSheet[self.miscCol + str(self.rowCount)] = part.dielectric
        self.currSheet[self.sizeCol + str(self.rowCount)] = part.size
        self.currSheet[self.toleranceCol + str(self.rowCount)] = part.tolerance
        self.currSheet[self.voltageCol + str(self.rowCount)] = part.voltage
        self.currSheet[self.quantityCol + str(self.rowCount)] = part.quantity
        #The Excel sheet is saved
        self.partList.save('output.xlsx')